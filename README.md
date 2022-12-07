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

# Projeto Airbnb Rio - Ferramenta de Previsão de Preço de Imóvel para Pessoas Físicas no município do Rio de Janeiro 
### Contexto

No Airbnb, qualquer pessoa que queira alugar por diária um imóvel ou um cômodo dele pode fazê-lo facilmente através de sua plataforma.

É criado um perfil de _host_ (pessoa que está alugando o imóvel por diária) e então cria-se o anúncio do imóvel.

Nesse anúncio, o _host_ deve descrever as características do imóvel da maneira mais detalhada possível, para que assim os locadores possam escolher o imóvel que melhor atenda às suas necessidades.

Há dezenas de personalizações possíveis de serem aplicadas ao anúncio, como quantidade de quartos, banheiros, se há TV a cabo, acesso à internet, os tipos de cama etc.

### Objetivo

Construir um modelo que gere uma sugestão de preço de diária para imóveis de médio padrão (nem muito caros nem muito baratos), baseando-se no histórico de preços e características dos imóveis disponíveis na base de dados.

Esse modelo poderá ser utilizado tanto para alguém que queira alugar seu imóvel, quanto para alguém que esteja interessado em ser um hóspide e queira conferir se o preço está acima, abaixo ou equivalente ao sugerido pelo modelo.

### O que temos disponível, inspirações e créditos

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

Essa solução é inspirada tanto na do Allan Bruno do kaggle no Notebook https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb quanto na solução desenvolvida no curso Python Impressionador da Hashtag.

- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

### Expectativas Iniciais

- Acredita-se que a sazonalidade pode ser um fator importante, visto que meses como dezembro costumam ser bem caros no Rio de Janeiro.
- A localização do imóvel deve fazer muita diferença no preço, já que no Rio de Janeiro a localização pode mudar completamente as características do lugar (segurança, beleza natural, pontos turísticos, acesso ao metrô).
- Adicionais/Comodidades podem ter um impacto significativo, visto que há muitos prédios e casas antigos no Rio de Janeiro.
