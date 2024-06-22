import pandas as pd
import folium
import json
import geopandas as gpd

# Load the crime data
data_file = 'D:/ASU_Bootcamp_Anaconda/Group-Project-4-main/Project_4_Userfacing/cyber_crime_data.csv'
data = pd.read_csv(data_file)

# Load the GeoJSON file
geojson_file = 'D:/ASU_Bootcamp_Anaconda/Group-Project-4-main/Project_4_Userfacing/WebsiteDesignResources/countries.geo.json'
with open(geojson_file) as f:
    geojson_data = json.load(f)

# Create a map
m = folium.Map(location=[20, 0], zoom_start=2, tiles='cartodb positron')

# Define the year and crime type selection
years = data['Year'].unique()
crime_types = data['CrimeType'].unique()

# Define the correct key for the country name
country_key = 'name'

# Function to generate the map for a specific year and crime type
def generate_map(year, crime_type):
    yearly_data = data[(data['Year'] == year) & (data['CrimeType'] == crime_type)]
    if yearly_data.empty:
        return
    
    # Merge data with GeoJSON based on country name
    gdf = gpd.GeoDataFrame.from_features(geojson_data["features"])
    merged = gdf.merge(yearly_data, left_on=country_key, right_on='Country', how='left')

    # Create a new GeoJSON with crime data
    geojson_merged = json.loads(merged.to_json())

    folium.Choropleth(
        geo_data=geojson_merged,
        name=f'{year} - {crime_type}',
        data=yearly_data,
        columns=['Country', 'Count'],
        key_on=f'feature.properties.{country_key}',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=f'Crime Count ({crime_type}, {year})',
        nan_fill_color='white',
        highlight=True,
        smooth_factor=0.5
    ).add_to(m)

# Generate initial map layers for each year and crime type
for year in years:
    for crime_type in crime_types:
        generate_map(year, crime_type)

# Save the map to an HTML file
map_output_file = 'D:/ASU_Bootcamp_Anaconda/Group-Project-4-main/Project_4_Userfacing/crime_map.html'
m.save(map_output_file)
