import json
import matplotlib.pyplot as plt

# Read the formatted data from the JSON file
with open('formatted_data.json', 'r') as json_file:
    formatted_data = json.load(json_file)

# Extract titles and plays data
titles = [item[0] for item in formatted_data]
plays_over_time = [item[1] for item in formatted_data]

# Create a line plot for each set of plays over time
for i in range(len(titles)):
    plt.plot(plays_over_time[i], label=titles[i])

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Plays')
plt.title('Plays Over Time')

# Add legend
plt.legend()

# Show the plot
plt.show()
