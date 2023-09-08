import json

# Read and parse the JSON data from the file
with open('plays_over_time.json', 'r') as json_file:
    data = json.load(json_file)

# Process the data into the desired format
formatted_data = []
for key, value in data.items():
    title = value['title']
    plays_over_time = [play[1] for play in value['plays']]
    formatted_data.append([title, plays_over_time])

# Write the formatted data to a new JSON file
output_filename = 'formatted_data.json'
with open(output_filename, 'w') as output_file:
    json.dump(formatted_data, output_file)

print(f"Formatted data has been written to {output_filename}")
