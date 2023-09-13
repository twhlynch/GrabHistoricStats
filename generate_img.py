import json
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))

with open('formatted_data.json', 'r') as json_file:
    formatted_data = json.load(json_file)

titles = [item[0] for item in formatted_data]
plays_over_time = [item[1] for item in formatted_data]

num_items = 30
sorted_data = sorted(range(len(plays_over_time)), key=lambda i: plays_over_time[i][-1], reverse=True)

top_maps = sorted_data[:num_items]
max_length = max(len(plays_over_time[i]) for i in top_maps)

for i in top_maps:
    data = plays_over_time[i]
    padding = max_length - len(data)
    data = [0] * padding + data
    plt.plot(data, label=titles[i])

plt.xlabel('Time')
plt.ylabel('Plays')
plt.title('Plays Over Time')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), labels=[titles[i] for i in top_maps])

plt.savefig('plays_over_time.png', bbox_inches='tight')
plt.close()
