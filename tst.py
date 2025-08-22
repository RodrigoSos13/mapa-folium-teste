import folium
import pandas as pd
import webbrowser
import requests
import os
import json

mapa=folium.Map(
    location=[-2.445406402677487, -54.72401972860755],
    zoom_start=6,
    control_scale=True,
)
# try:
#    url = f"https://api-redemet.decea.mil.br/produtos/satelite/realcada?api_key=YMBFKSHNjZuVi818AciGHd3D4ZE7Tc0XOf0rl1Vo&data=2020032114"
#     response = requests.get(url)
#     if response.status_code == 200:
#         dados = response.json()
        
#         if "satelite" in dados["data"]:
#             sat_info = dados["data"]["satelite"][0] 
#             path = sat_info["path"]
#             data = sat_info["data"]

#             lat_min = float(dados["data"]["lat_lon"]["lat_min"])
#             lat_max = float(dados["data"]["lat_lon"]["lat_max"])
#             lon_min = float(dados["data"]["lat_lon"]["lon_min"])
#             lon_max = float(dados["data"]["lat_lon"]["lon_max"])

#             folium.raster_layers.ImageOverlay(
#                 name=f"Satélite {data}",
#                 image=path,
#                 bounds=[[lat_min, lon_min], [lat_max, lon_max]],
#                 opacity=0.6
#             ).add_to(mapa)
# except Exception as e:
#     print(f'Cota da API atingida.')


folium.LayerControl().add_to(mapa)

folium.Marker(
    [-2.4202489970104, -54.74069530441131],
    popup='Ufopa',
    tooltip='Click Aqui'
).add_to(mapa)

folium.Marker(
    [-4.263859396979959, -55.98976250904246],
    popup='Itaituba',
    tooltip='lugar legal',
    icon=folium.Icon(color='green')
).add_to(mapa)

folium.Marker(
    [-3.2040380145516147, -52.20384868594255],
    popup='Altamira',
    tooltip='só para testar',
    icon=folium.Icon(color='black')
).add_to(mapa)

# folium.CircleMarker(
#     [-20.9226, -47.8304],
#     radius=50,
#     color='red',
#     fill_color='red'
# ).add_to(mapa)


# df = pd.read_excel('coordenadas.xlsx')
# for local, lat, lon in zip(df.LOCAL, df.LATITUDE.values, df.LONGITUDE.values):
#     folium.Marker([lat,lon], tooltip=f'{local}').add_to(mapa)

pins = json.load(open('pins-estacoes.json', 'r'))
print(pins)

for pin in pins:
    folium.Marker(
        [pin['LAT'], pin['LONG']],
        tooltip=f'{pin['LOCAL']}',
        # icon=folium.Icon(color=pin.get('color', 'blue'))
    ).add_to(mapa)

#mapa.add_child(folium.LatLngPopup())

html = "mapa.html"
mapa.save(html)


caminho_html = os.path.abspath(html)
webbrowser.open(f"file://{caminho_html}")