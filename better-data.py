import json
import matplotlib.pyplot as plt

# Read the formatted data from the JSON file
with open('formatted_data.json', 'r') as json_file:
    formatted_data = json.load(json_file)

# Sort the data based on the last value of the plays array for each title
sorted_data = sorted(formatted_data, key=lambda x: x[1][-1], reverse=True)

# Find the longest dataset
longest_data = max(sorted_data, key=lambda x: len(x[1]))

# Initialize variables for the top 100 data
top_100_data = []
count = 0

# Extract titles and plays data for the top 100, adding zeros to match the longest dataset
for item in sorted_data:
    if count >= 100:
        break

    title, plays = item[0], item[1]
    start_index = next((i for i, val in enumerate(plays) if val != 0), 0)

    # Find the difference in length and add zeros to the start
    length_difference = len(longest_data[1]) - len(plays)
    padded_plays = [0] * length_difference + plays

    top_100_data.append([title, padded_plays])
    count += 1

# Create a line plot for each set of plays over time
for i in range(len(top_100_data)):
    title, plays = top_100_data[i]
    plt.plot(plays, label=title)

# Set labels and title
plt.xlabel('Time')
plt.ylabel('Plays')
plt.title('Top 100 Plays Over Time (Highest Scores at Ends)')

# Add legend
plt.legend()

# Show the plot
plt.show()
