
# coding: utf-8

# In[1]:


#Modules used
import pandas as pd
import folium
from sodapy import Socrata

#Accessing data from Socrata - Real time Traffic
client = Socrata("data.cityofnewyork.us","CEjJtZpnruNltsucUPQkL4szd")
results_list = client.get("i4gi-tjb9",select="travel_time,speed,borough,link_points")
results_df = pd.DataFrame.from_records(results_list)
df = pd.DataFrame.from_dict(results_df)
df.head()
#display(df) - used to display the whole data frame(raw data)

#Grouping of the data according to the borough and calculating the mean speed
groupby_borough = df['speed'].groupby(df['borough'])
groupby_borough
df.speed = df.speed.astype(float)
df['speed'].dtype
list(df['speed'].groupby(df['borough']))
#df.groupby('borough')['speed'].mean()
average_speed=df.groupby('borough')['speed'].mean().values.tolist()

#Grouping of the data according to the borough and calculating the mean speed
groupby_borough = df['travel_time'].groupby(df['borough'])
groupby_borough
df.travel_time = df.travel_time.astype(float)
df['travel_time'].dtype
list(df['travel_time'].groupby(df['borough']))
#df.groupby('borough')['speed'].mean()
average_travel_time=df.groupby('borough')['travel_time'].mean().values.tolist()


# Dataframe with the Lat, long, name of the cities and average speed for mapping
data = pd.DataFrame({
   'lat':[40.8448,40.6782,40.7831,40.7282,40.5795,40.5795],
   'lon':[-73.8648,-73.9442,-73.9712,-73.7949,-74.1502,-74.1502],
   'name':['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'Staten island'],
   'value_speed':average_speed,
    'value_time':average_travel_time
})
data
display(data)

#Folium maps for the display of the final output
map = folium.Map(location=[40.7128, -74.0060],tiles="openstreetmap",zoom_start=10)
for i in range(0,len(data)):
    folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=data.iloc[i]['name']).add_to(map)

# Adding marker one by one
for i in range(0,len(data)):
    folium.Circle(location=[data.iloc[i]['lat'], data.iloc[i]['lon']],popup=data.iloc[i]['name'],radius=data.iloc[i]['value_speed']*100,color='crimson',fill=True,fill_color='crimson' ).add_to(map)    
display(map)

#Folium maps for the display of the final output
map = folium.Map(location=[40.7128, -74.0060],tiles="openstreetmap",zoom_start=10)
for i in range(0,len(data)):
    folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=data.iloc[i]['name']).add_to(map)

# Adding marker one by one
for i in range(0,len(data)):
    folium.Circle(location=[data.iloc[i]['lat'], data.iloc[i]['lon']],popup=data.iloc[i]['name'],radius=data.iloc[i]['value_time']*5,color='yellow',fill=True,fill_color='yellow' ).add_to(map)
display(map)

