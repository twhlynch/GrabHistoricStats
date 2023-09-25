import json
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))

with open('formatted_data.json', 'r') as json_file:
    formatted_data = json.load(json_file)

titles = [item[0] for item in formatted_data]
plays_over_time = [item[1] for item in formatted_data]

# Calculate the highest value ever for each item
highest_values = [max(item) for item in plays_over_time]

# Sort items by their final value
sorted_data = sorted(range(len(plays_over_time)), key=lambda i: plays_over_time[i][-1], reverse=True)

# Sort the sorted_data by their highest value ever
sorted_data = sorted(sorted_data, key=lambda i: highest_values[i], reverse=True)

# Select the top 30 items
num_items = 30
top_maps = sorted_data[:num_items]

max_length = max(len(plays_over_time[i]) for i in top_maps)

for i in top_maps:
    data = plays_over_time[i]
    padding = max_length - len(data)
    data = [0] * padding + data
    plt.plot(data, label=titles[i])

plt.xlabel('Time')
plt.ylabel('Plays')
plt.title('Plays Over Time (Top 30 by Highest Value Ever)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), labels=[titles[i] for i in top_maps])

plt.savefig('plays_over_time_highest.png', bbox_inches='tight')
plt.close()
