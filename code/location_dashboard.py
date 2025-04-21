import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("Syracuse Parking Tickets by Location")

# Load the cleaned data
df = pd.read_csv('./cache/tickets_in_top_locations.csv')

# Sidebar for location selection
selected_location = st.sidebar.selectbox("Choose a location", sorted(df['location'].unique()))

# Filter data to just this location
filtered = df[df['location'] == selected_location]

# Compute metrics
total_tickets = len(filtered)
total_fines = filtered['amount'].sum()

# Layout: Two columns for metrics
col1, col2 = st.columns(2)
col1.metric("Total Tickets", f"{total_tickets:,}")
col2.metric("Total Fines ($)", f"${total_fines:,.2f}")

# Layout: 3 columns for charts and map
chart_col1, chart_col2, map_col = st.columns([1.5, 1.5, 1])

# Bar Chart: Distribution by day of week
with chart_col1:
    st.subheader("Tickets by Day of Week")
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day_counts = filtered['dayofweek'].value_counts().reindex(day_order).fillna(0)
    fig, ax = plt.subplots()
    sns.barplot(x=day_counts.index, y=day_counts.values, ax=ax)
    ax.set_ylabel("Tickets")
    ax.set_xlabel("Day of Week")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Line Chart: Distribution by hour
with chart_col2:
    st.subheader("Tickets by Hour of Day")
    hour_counts = filtered['hourofday'].value_counts().sort_index()
    fig2, ax2 = plt.subplots()
    sns.lineplot(x=hour_counts.index, y=hour_counts.values, ax=ax2, marker="o")
    ax2.set_xlabel("Hour")
    ax2.set_ylabel("Tickets")
    st.pyplot(fig2)

# Map with location
with map_col:
    st.subheader("Ticket Location")
    location_map = filtered[['lat', 'lon']].drop_duplicates()
    st.map(location_map.rename(columns={"lat": "latitude", "lon": "longitude"}))
