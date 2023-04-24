import pandas as pd
import osmnx as ox

df=pd.read_csv(r"C:\Users\DNS\Desktop\Flask_Turism\yes_2.csv",delimiter=",") #,encoding = 'unicode_escape')

#
df_cut=df[['название.объекта','POINT_X','POINT_Y']]

r = 0

#russia_map = folium.Map(location = [54.98848, 73.32424],zoom_start = 6)
# location where you want to find your route
place = 'Omsk, Russia'

# find shortest route based on the mode of travel
mode = 'walk' # 'drive', 'bike', 'walk'

# find shortest path based on distance or time
optimizer = 'time' # 'length','time'

# create graph from OSM within the boundaries of some 
# geocodable place(s)
russia_map = ox.graph_from_place(place, network_type = mode)