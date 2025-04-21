import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd

# Constants
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min fine amount
VMAX = 5000                 # max fine amount

st.set_page_config(layout="wide")
st.title("Heatmap of Syracuse Parking Ticket Hotspots")

# Load the data
df = pd.read_csv('./cache/top_locations_mappable.csv')

# Normalize amount for circle size and color
def scale_amount(val, vmin=VMIN, vmax=VMAX):
    """Scale value between 0 and 1 for color/size mapping"""
    return min(max((val - vmin) / (vmax - vmin), 0), 1)

# Create Folium map centered on Syracuse
m = folium.Map(location=CUSE, zoom_start=ZOOM)

# Add circle markers for each location
for _, row in df.iterrows():
    amount = row['amount']
    scale = scale_amount(amount)
    folium.CircleMarker(
        location=(row['lat'], row['lon']),
        radius=5 + (scale * 10),  # Size varies with amount
        color='red',
        fill=True,
        fill_opacity=0.6,
        popup=f"{row['location']}<br>Amount: ${amount:,.2f}"
    ).add_to(m)

# Render the map in Streamlit
sf.folium_static(m, width=1100, height=700)
