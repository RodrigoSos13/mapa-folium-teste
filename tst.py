import folium
import pandas as pd
import webbrowser
import os

mapa=folium.Map(
    location=[-2.445406402677487, -54.72401972860755],
    zoom_start=6,
    control_scale=True,
)

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

folium.CircleMarker(
    [-20.9226, -47.8304],
    radius=50,
    color='red',
    fill_color='red'
).add_to(mapa)

rota=[
    (-2.5178, -54.6982),
    ( -2.6934, -54.7531),
    (-3.2941, -54.7723),
    ( -3.6121, -54.9728),
    (-4.0780, -55.3711),
    (-4.3190,  -55.9149)
]

df = pd.read_excel('dados.xlsx')
for local, lat, lon in zip(df.LOCAL, df.LATITUDE.values, df.LONGITUDE.values):
    folium.Marker([lat,lon], tooltip=f'{local}').add_to(mapa)


folium.PolyLine(rota, tooltip='Rota').add_to(mapa)

mapa.add_child(folium.LatLngPopup())

html = "mapa.html"
mapa.save(html)


caminho_html = os.path.abspath(html)
webbrowser.open(f"file://{caminho_html}")