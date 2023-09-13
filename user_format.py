import json

# Read and parse the JSON data from the file
with open('plays_over_time.json', 'r') as json_file:
    data = json.load(json_file)

# Process the data into the desired format
formatted_data = []
for key, value in data.items():
    id = value['levelId'].split(':')[0]
    plays_over_time = [play[1] for play in value['plays']]
    for i in range(len(formatted_data)):
        if formatted_data[i][0] == id:
            if len(formatted_data[i][1]) > len(plays_over_time):
                # pad left with zeros
                padding = len(formatted_data[i][1]) - len(plays_over_time)
                plays_over_time = [0] * padding + plays_over_time
            elif len(formatted_data[i][1]) < len(plays_over_time):
                # pad right with zeros
                padding = len(plays_over_time) - len(formatted_data[i][1])
                formatted_data[i][1] = formatted_data[i][1] + [0] * padding
            
            formatted_data[i][1] = [sum(x) for x in zip(formatted_data[i][1], plays_over_time)]
            break
    else:
        formatted_data.append([id, plays_over_time])

# Write the formatted data to a new JSON file
output_filename = 'formatted_users.json'
with open(output_filename, 'w') as output_file:
    json.dump(formatted_data, output_file)

print(f"Formatted data has been written to {output_filename}")
