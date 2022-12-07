#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor
from sklearn.model_selection import train_test_split

dataset_path = pathlib.Path(r'dataset')
database_airbnb = pd.DataFrame()
months = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8,
         'set':9, 'out':10, 'nov':11, 'dez':12} #months' dictionary and its numbers
#reading and unifying csv files
for csv_file in dataset_path.iterdir():
    df = pd.read_csv(dataset_path / csv_file.name)
    
    month_name = csv_file.name[:3] #selecting the first 3 characters to get the month name
    month = months[month_name] #using the dictionary to get the month number
    year = csv_file.name[-8:] #catching the last 8 characters
    year = int(year.replace('.csv','')) #removing '.csv' to keep only the year
    
    df['year'] = year #adding year column
    df['month'] = month #adding month column
    
    database_airbnb = database_airbnb.append(df) #adding datas in the dataframe

#After a qualitative analysis, we'll keep the following columns: 
columns = ['bedrooms', 'latitude', 'longitude', 'amenities', 'accommodates', 'minimum_nights',
           'bathrooms', 'beds','room_type', 'host_listings_count', 'instant_bookable',
           'cancellation_policy', 'host_is_superhost', 'property_type','year', 'month',
           'bed_type', 'price']

database_airbnb = database_airbnb.loc[:, columns]

dabase_airbnb = database_airbnb.dropna() #default axis=0 -> removing null lines

#adjusting price column
database_airbnb['price'] = database_airbnb['price'].str.replace('$','') #removing $
database_airbnb['price'] = database_airbnb['price'].str.replace(',','') #removing ,
database_airbnb['price'] = database_airbnb['price'].astype(np.float32) #transforming in float

def limits(column):
    #separating quartiles
    q1 = column.quantile(0.25) #first quartile
    q3 = column.quantile(0.75) #third quartile
    amplitude = q3 - q1
    inf_lim = q1 - 1.5*amplitude
    sup_lim = q3 + 1.5*amplitude
    return inf_lim, sup_lim

def delete_outliers(df, column_name):
    lim_inf, lim_sup = limits(df[column_name])
    df = df.loc[((df[column_name]>=lim_inf) & (df[column_name]<=lim_sup)), :] #columns in the limits
    return df

database_airbnb = delete_outliers(database_airbnb, 'price')
database_airbnb = delete_outliers(database_airbnb, 'host_listings_count')
database_airbnb = delete_outliers(database_airbnb, 'accommodates')
database_airbnb = delete_outliers(database_airbnb, 'bathrooms')
database_airbnb = delete_outliers(database_airbnb, 'bedrooms')
database_airbnb = delete_outliers(database_airbnb, 'beds')
database_airbnb = delete_outliers(database_airbnb, 'minimum_nights')

#Grouping values under 2000
property_table = database_airbnb['property_type'].value_counts()
grouping_columns = []

for property in property_table.index:
    if property_table[property] < 2000:
        grouping_columns.append(property)

for property in grouping_columns:
    database_airbnb.loc[database_airbnb['property_type']==property, 'property_type'] = 'Outher'

beds_table = database_airbnb['bed_type'].value_counts()

grouping_columns = []

for bed in beds_table.index:
    if bed != 'Real Bed':
        grouping_columns.append(bed)

for bed in grouping_columns:
    database_airbnb.loc[database_airbnb['bed_type']==bed, 'bed_type'] = 'Outher'

table_cancellation = database_airbnb['cancellation_policy'].value_counts()
grouping_columns = []

for cancellation in table_cancellation.index:
    if table_cancellation[cancellation] < 10000:
        grouping_columns.append(cancellation)

for cancellation in grouping_columns:
    database_airbnb.loc[database_airbnb['cancellation_policy']==cancellation, 'cancellation_policy'] = 'strict'

#Adding 'num_amenities' column
database_airbnb['num_amenities'] = database_airbnb['amenities'].str.split(',').apply(len)

#Removing amenities column
database_airbnb = database_airbnb.drop('amenities', axis=1)

lines_qnt = delete_outliers(database_airbnb, 'num_amenities')

#Encoding

tf_columns = ['host_is_superhost','instant_bookable']
category_columns = ['property_type', 'room_type', 'bed_type', 'cancellation_policy']

database_airbnb_cod = database_airbnb.copy()
for column in tf_columns:
    database_airbnb_cod.loc[database_airbnb_cod[column]=='t', column] = 1
    database_airbnb_cod.loc[database_airbnb_cod[column]=='f', column] = 0

database_airbnb_cod = pd.get_dummies(data=database_airbnb_cod, columns=category_columns)

#Prediction model
def evaluate_model(model_name, y_test, prediction):
    r2 = r2_score(y_test, prediction)
    RSME = np.sqrt(mean_squared_error(y_test, prediction))
    return f'Modelo {model_name}: \nR²: {r2:.2%}\nRSME: {RSME:.2f}'

X = database_airbnb_cod.drop('price', axis=1)
y = database_airbnb_cod['price']
et_model = ExtraTreesRegressor()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)

et_model.fit(X_train, y_train)

prediction = et_model.predict(X_test)

print(evaluate_model('ExtraTrees', y_test, prediction))