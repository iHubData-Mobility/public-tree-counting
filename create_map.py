import pandas as pd
import haversine as hs
import pickle
import folium
import os
import webbrowser
from folium.plugins import FloatImage

def calculate_distance(points):
    length = len(points)
    step = 20
    prev_location = points[0]
    distance = 0
    for i in range(step, length, step):
      curr_location = points[i]
      temp_distance = hs.haversine(prev_location, curr_location)
      distance = distance + temp_distance
      prev_location = curr_location 
    print(distance)
    return distance

def display(mymap, points, distance, tree_count):
  thresh1 = int(t1 * distance)
  thresh2 = int(t2 * distance)
  thresh3 = int(t3 * distance)
  thresh4 = int(t4 * distance)
  print("Thresholds: ", thresh1, thresh2, thresh3, thresh4)
  if tree_count < thresh1:
    print("1")
    folium.PolyLine(points, color='black', weight=4.5, opacity=.9).add_to(mymap) 
  elif tree_count < thresh2:
    print("2")
    folium.PolyLine(points, color='#ed3833', weight=4.5, opacity=.9).add_to(mymap) 
  elif tree_count < thresh3:
    print("3")
    folium.PolyLine(points, color='#2070c0', weight=4.5, opacity=.9).add_to(mymap)
  elif tree_count < thresh4:
    print("4")
    folium.PolyLine(points, color='#70ed3e', weight=4.5, opacity=.9).add_to(mymap)
  else:
    print("5")
    folium.PolyLine(points, color='#548236', weight=4.5, opacity=.9).add_to(mymap)

t1 = 20
t2 = 30
t3 = 40
t4 = 50

if os.path.exists('gps_points.txt'):
    mymap = folium.Map( location=[17.387140, 78.491684], zoom_start=13, tiles=None)
    #folium.TileLayer('openstreetmap', name='OpenStreet Map').add_to(mymap)
    folium.TileLayer('cartodbpositron').add_to(mymap)
    image_file = 'legend.png'
    FloatImage(image_file, bottom=0, left=86).add_to(mymap)
    
    with open('gps_points.txt', 'rb') as file:
        gps_list = pickle.load(file)
        print("Loaded: ", len(gps_list))
        for route in gps_list:
            tree_count, gps_points = route
            print(tree_count, len(gps_points))
            total_distance = calculate_distance(gps_points)
            display(mymap, gps_points, total_distance, int(tree_count))
        filepath = 'map.html'
        mymap.save(filepath)
else:
    print("No gps points to display")
