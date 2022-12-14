# Airbnb Rio Project - A Tool for Predict the Price of Properties in Rio de Janeiro city for common people
### Context

On Airbnb, any person who wants to rent daily a property or a room can do that easily using its platform.

A _host_ profile is created, after that, the property advertisement can be posted.

In this advertisement, the _host_ must describe the property features with details,in this way the lessors can choose the best property to fulfil its necessities.

There are many personalizations to be added in the advertisement, as bedrooms/bathrooms quantity, if it has TV, Wifi, the bed types etc.

### Goal
Bild a model to generate a price sugestion for the daily rent of regular properties (neither extra expensives nor too cheaps), based on the prices during a time interval (for the properties availble in the dataset).

Either the person who wants to rent a property or the one who needs to pay for it will be able to use this model. It will help them both to compare prices and make smart choices.

### What we have available, inspirations and credities

The dataset is from the kaggle website: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

This soluction is inspired in the Allan Bruno soluction (in his Kaggle Notebook https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb) and in the soluction developed in the course "Python Impressionador" from Hashtag.

- The datasets are the prices and features of the properties in each month.
- The prices are in Brazilian reais (R$).
- The datasets are from 2018 April until 2020 May, except 2018 june.

### Initial Expectations

- It's believed that seasonality may be an important factor, as months like December tend to be very expensive in Rio de Janeiro.
- The property location may change the price, as the location in Rio can modify completely the features of the place (security, natural beauty, tourist highlights, easy metro access etc.)
- Amenities may have a significant impact, as there are many old buildings in Rio de Janeiro.

# Projeto Airbnb Rio - Ferramenta de Previs??o de Pre??o de Im??vel para Pessoas F??sicas no munic??pio do Rio de Janeiro 
### Contexto

No Airbnb, qualquer pessoa que queira alugar por di??ria um im??vel ou um c??modo dele pode faz??-lo facilmente atrav??s de sua plataforma.

?? criado um perfil de _host_ (pessoa que est?? alugando o im??vel por di??ria) e ent??o cria-se o an??ncio do im??vel.

Nesse an??ncio, o _host_ deve descrever as caracter??sticas do im??vel da maneira mais detalhada poss??vel, para que assim os locadores possam escolher o im??vel que melhor atenda ??s suas necessidades.

H?? dezenas de personaliza????es poss??veis de serem aplicadas ao an??ncio, como quantidade de quartos, banheiros, se h?? TV a cabo, acesso ?? internet, os tipos de cama etc.

### Objetivo

Construir um modelo que gere uma sugest??o de pre??o de di??ria para im??veis de m??dio padr??o (nem muito caros nem muito baratos), baseando-se no hist??rico de pre??os e caracter??sticas dos im??veis dispon??veis na base de dados.

Esse modelo poder?? ser utilizado tanto para algu??m que queira alugar seu im??vel, quanto para algu??m que esteja interessado em ser um h??spide e queira conferir se o pre??o est?? acima, abaixo ou equivalente ao sugerido pelo modelo.

### O que temos dispon??vel, inspira????es e cr??ditos

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

Essa solu????o ?? inspirada tanto na do Allan Bruno do kaggle no Notebook https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb quanto na solu????o desenvolvida no curso Python Impressionador da Hashtag.

- As bases de dados s??o os pre??os dos im??veis obtidos e suas respectivas caracter??sticas em cada m??s.
- Os pre??os s??o dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exce????o de junho de 2018 que n??o possui base de dados

### Expectativas Iniciais

- Acredita-se que a sazonalidade pode ser um fator importante, visto que meses como dezembro costumam ser bem caros no Rio de Janeiro.
- A localiza????o do im??vel deve fazer muita diferen??a no pre??o, j?? que no Rio de Janeiro a localiza????o pode mudar completamente as caracter??sticas do lugar (seguran??a, beleza natural, pontos tur??sticos, acesso ao metr??).
- Adicionais/Comodidades podem ter um impacto significativo, visto que h?? muitos pr??dios e casas antigos no Rio de Janeiro.
