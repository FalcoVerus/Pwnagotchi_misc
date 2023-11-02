# pip install folium
import folium
import os
import json

def read_geo_files(geo_dir):
    if not os.path.exists(geo_dir):
        print('Directory does not exists.')
        return
    
    map_object = folium.Map(location=[47.41, 19.25], zoom_start=10)
    
    for geo_file in os.listdir(geo_dir):
        geo_file_path = os.path.join(geo_dir, geo_file)
        
        if os.path.isfile(geo_file_path) and geo_file.endswith(".geo.json"):
            with open(geo_file_path, 'r', encoding='utf-8') as geo_f:
                geo_json = json.load(geo_f)
                lat = geo_json['location']['lat']
                lng = geo_json['location']['lng']
                location = [lat, lng]
                
                wifi_name = os.path.splitext(geo_file)[0]
# Add a marker at the specified coordinates
                folium.Marker(location=location, popup=wifi_name).add_to(map_object)
# Save the map to an HTML file
    map_object.save('wifi_tracker_map.html')

geo_dir = r'D:\Stuff\Security\Networking\handshakes'
read_geo_files(geo_dir)

