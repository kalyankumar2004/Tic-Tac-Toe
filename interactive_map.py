import folium
import pandas as pd
import webbrowser
import os

# Load CSV data
data = pd.read_csv("locations.csv")

# Create map centered at average location
map_center = [data["latitude"].mean(), data["longitude"].mean()]
my_map = folium.Map(location=map_center, zoom_start=13)

# Add markers with image popups
for _, row in data.iterrows():
    html_popup = f"""
    <h4>{row['name']}</h4>
    <p>{row['description']}</p>
    <img src="{row['image']}" width="200">
    """
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=folium.Popup(html_popup, max_width=250),
        tooltip=row["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(my_map)

# Save and open the map
file_name = "map_with_images.html"
my_map.save(file_name)
webbrowser.open('file://' + os.path.realpath(file_name))

print("✅ Map with image popups created and opened.")
