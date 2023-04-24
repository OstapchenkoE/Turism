import osmnx as ox
import networkx as nx
#import pandas as pd
import folium
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition
from folium.features import DivIcon
from math import sin, cos, sqrt, atan2, radians
import random
import time
import sys 

#print("he")

def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


from eternity import russia_map,df,df_cut


#from app import kol,name
#kol=int(5)
optimizer = 'time'
def algoritm(name,kol):
    first_landmark =name
    n =int(kol)
    route=[]


    #ищим памятники в радиусе 1км от first_landmark
    for i in range(len(df)):
      #находим строку в исходной таблице с названием first_landmark
      if df.iloc[i,4]==first_landmark:
      #добавляем метку first_landmark на карту 
        r=i  
    landmarks=[]  
    for i in range(len(df)):
      coordinates = [[df.iloc[r,7],df.iloc[r,6]],
                    [df.iloc[i,7],df.iloc[i,6]]]


      distance = calculate_distance(coordinates[0][0], coordinates[0][1],
                                    coordinates[1][0], coordinates[1][1])
      if distance < 1:
        #если памятник находится в радиусе километр то добавляем его название и координаты  в landmarks
        landmark = []
        landmark.append(df_cut.iloc[i,0])
        landmark.append(df_cut.iloc[i,1])
        landmark.append(df_cut.iloc[i,2])
        landmarks.append(landmark)


    random_landmarks = []
    #добавляем first_landmark в random_landmarks
    landmark = []
    landmark.append(df_cut.iloc[r,0])
    landmark.append(df_cut.iloc[r,1])
    landmark.append(df_cut.iloc[r,2])
    random_landmarks.append(landmark)
    #начало время работы программы 
    start=time.time()
    # выберем n-1 памятник рандомно в радиусе 1км
    while len(random_landmarks)<n:
      if time.time()-start>0.2:
        sys.exit("недостаточно памятников в радиусе 1км")
      random_index = random.randint(0, len(landmarks) - 1)
      if landmarks[random_index] not in random_landmarks:
        random_landmarks.append(landmarks[random_index])

    for i in range(1,len(random_landmarks)):
      # find the nearest node to the start location
      orig_node = ox.get_nearest_node(russia_map, (random_landmarks[i-1][2],random_landmarks[i-1][1]))

    # find the nearest node to the end location
      dest_node = ox.get_nearest_node(russia_map, (random_landmarks[i][2],random_landmarks[i][1]))

    # find the shortest path
      shortest_route=nx.shortest_path(russia_map, orig_node,dest_node,
                                      weight=optimizer)
      if i!=len(random_landmarks)-1:
        route.extend(shortest_route[:-1])
      else:
        route.extend(shortest_route)
    shortest_route_map = ox.plot_route_folium(russia_map,route)
    for i in range(0,len(random_landmarks)):  
      start_marker = folium.Marker(
                location = (random_landmarks[i][2],random_landmarks[i][1]),
                popup = (random_landmarks[i][0]),
                icon = folium.Icon(color='green'))
      start_marker.add_to(shortest_route_map)
    return shortest_route_map