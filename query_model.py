import geopandas as gpd
import pandas as pd
import json

with open('at_turaif.geojson') as f:
    data = json.load(f)

interest_keys = ['tourism', 'amenity', 'leisure']
interest_values = ['cafe', 'restaurant', 'museum', 'park', 'information']

filtered_data = []

for feature in data['features']:
    properties = feature['properties']
    for key in interest_keys:
        if key in properties and properties[key] in interest_values:
            # Extract and append the name, value, and field to the list
            if properties.get('name', 'N/A') == 'N/A':
                print(properties)
            filtered_data.append({
                'name': properties.get('name', 'N/A'),
                'value': properties[key],
                'field': key
            })

# Convert the filtered data into a DataFrame
df = pd.DataFrame(filtered_data)

# Save the DataFrame to a CSV file
df.to_csv('at_turaif_model.csv', index=False)