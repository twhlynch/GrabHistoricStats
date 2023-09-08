import json
import matplotlib.pyplot as plt

# Read the formatted data from the JSON file
with open('formatted_data.json', 'r') as json_file:
    formatted_data = json.load(json_file)

# Sort the data based on the last value of the plays array for each title
sorted_data = sorted(formatted_data, key=lambda x: x[1][-1], reverse=True)

# Take the top 100 entries
top_100_data = sorted_data[:100]

# Extract titles and plays data for the top 100
titles = [item[0] for item in top_100_data]
plays_over_time = [item[1] for item in top_100_data]

# Create a line plot for each set of plays over time
for i in range(len(titles)):
    plt.plot(plays_over_time[i], label=titles[i])

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Plays')
plt.title('Top 100 Plays Over Time (Highest Scores at Ends)')

# Add legend
plt.legend()

# Show the plot
plt.show()
