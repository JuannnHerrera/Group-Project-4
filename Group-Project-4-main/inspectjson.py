import json

geojson_file = 'D:/ASU_Bootcamp_Anaconda/Group-Project-4-main/Project_4_Userfacing/WebsiteDesignResources/countries.geo.json'
with open(geojson_file) as f:
    geojson_data = json.load(f)

# Print the first feature to inspect the properties
print(geojson_data['features'][0]['properties'])
