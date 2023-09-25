import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Load data from JSON file
with open('formatted_data.json', 'r') as json_file:
    formatted_data = json.load(json_file)

# Extract titles and plays_over_time
titles = [item[0] for item in formatted_data]
plays_over_time = [item[1] for item in formatted_data]

num_items_to_show = 10  # Number of items to show in the legend and on the plot
max_length = max(len(data) for data in plays_over_time)

# Initialize a figure and axes for the animation
fig, ax = plt.subplots(figsize=(12, 8))

# Create a function to update the plot at each frame
def update(frame):
    ax.clear()

    # Sort items by plays at the current frame
    plays_at_frame = [data[frame] if frame < len(data) else 0 for data in plays_over_time]
    sorted_indices = np.argsort(plays_at_frame)[::-1][:num_items_to_show]

    # Plot the top 10 items at the current frame
    for i in sorted_indices:
        data = plays_over_time[i]
        padding = max_length - len(data)
        data = [0] * padding + data
        plt.plot(data, label=titles[i])

    plt.xlabel('Time')
    plt.ylabel('Plays')
    plt.title(f'Plays Over Time - Frame {frame + 1}')
    plt.legend(loc='upper left', labels=[titles[i] for i in sorted_indices[:num_items_to_show]])

# Create an animation
ani = animation.FuncAnimation(fig, update, frames=max_length, repeat=False)

# Display the animation in Jupyter Notebook or standalone Python script
plt.show()
