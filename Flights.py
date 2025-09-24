import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

data = pd.read_csv(r"airlines_flights_data.csv")
data

#Cleaning the data

data.drop(columns = 'index', inplace = True)
data.info()
data.describe()

data[data['duration'] == 39.670000 ]
data[data['duration'] == 1.920000 ]
data[data['price'] == 35145.000000 ]
data[data['price'] == 1998.000000 ]

data.isnull().sum()

data.head()

data['airline'].nunique()
data['airline'].unique()

#Showing all the airlines with their frequencies
data['airline'].value_counts()

#Showing all the airlines with their number of flights in horizontal bar graph
data['airline'].value_counts(ascending = True).plot.barh(color=['green', 'blue'])
plt.xlabel('Number of Flights')
plt.ylabel('Airlines')
plt.title('Airline with frequencies')
plt.show()

#Showing the departure time of the flights
data['departure_time'].value_counts()

#Showing the arrival time of the flights
data['arrival_time'].value_counts()

#Showing the Deprature time & Arrival time for the flights with their counts
plt.figure(figsize=(16,4))
plt.subplot(1,2,1)

plt.bar(data['departure_time'].value_counts().index, data['departure_time'].value_counts().values, color=['r','b'])
plt.xlabel('D. Time')
plt.ylabel('D. freq')
plt.title('Departure Time')

plt.subplot(1,2,2)
plt.bar(data['arrival_time'].value_counts().index, data['arrival_time'].value_counts().values, color=['g','y'])
plt.xlabel('A. Time')
plt.ylabel('A. freq')
plt.title('Arrival Time')
plt.show()

#showing the source city of the  flights
data['source_city'].value_counts()

#showing the destination city of the  flights
data['destination_city'].value_counts()

#showing the soruce city & destination city	for the flights with their counts
plt.figure(figsize=(16,4))

#It is not important to figure the graph of the Source city, because there is on Source city: Delhi
#plt.subplot(1,2,1)

#plt.barh(data['source_city'].value_counts().index, data['source_city'].value_counts().values)
#plt.xlabel('No. of flights')
#plt.ylabel('Cities')
#plt.title('Source City with no. of flights')

plt.subplot(1,2,2)
plt.barh(data['destination_city'].value_counts().index, data['destination_city'].value_counts().values, color=['y','r'])
plt.xlabel('No. of flights')
plt.ylabel('Cities')
plt.title('Destination City with no. of flights')
plt.show()


#Grouping the airlines and checking the mean price
data.groupby('airline')['price'].mean()

#Draw a categorical plot showing the Mean ticket price for each airline
sns.catplot(x='airline', y='price', data=data, kind='bar', palette='rocket')
plt.show()

#Checking the Mean ticket price based on the Dep. time
data.groupby('departure_time')['price'].mean()

#Checking the Mean ticket price based on the Arrival time
data.groupby('arrival_time')['price'].mean()

sns.catplot(x='departure_time', y='price', data=data, kind='bar', palette='rocket')
plt.show()

sns.catplot(x='arrival_time', y='price', data=data, kind='bar', palette='rocket')
plt.show()

sns.relplot(x='arrival_time', y='price', data=data, col='departure_time', kind='line')
plt.show()

#Checking the Mean ticket price for each source city
data.groupby('source_city')['price'].mean()

data.groupby('destination_city')['price'].mean()

sns.relplot(x='destination_city', y='price', data=data, col='source_city', kind='line')
plt.show()


data['days_left'].nunique()
data['days_left'].unique()

#Checking the Mean ticket price for different days left
data.groupby('days_left')['price'].mean()

sns.relplot(x='days_left', y='price', data=data, kind='line')
plt.show()


data['class'].unique()

 x = data[data['class'] == 'Economy']
 x

x.price.mean()

#What will be the average price of Vistara airline for a flight for Delhi to Hyderabad in Economy class?

data.head(1)

new_data = data[(data['airline'] == 'Vistara') & (data['source_city'] == 'Delhi') & (data['destination_city'] == 'Hyderabad') & (data['class'] == 'Economy')]

new_data

new_data['price'].mean()

