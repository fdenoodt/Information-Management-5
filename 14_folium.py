import folium
import webbrowser

svmap = folium.Map(location=[37, -122], titles="Stamen terrain", zoom_start=11)
folium.CircleMarker([37, -122], popup="cisco systems", color="#0F8ABE").add_to(svmap)

filepath = 'C:\\temp\\map.html'
svmap.save(filepath)
webbrowser.open('file://' + filepath)
