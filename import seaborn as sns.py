import seaborn as sns
import matplotlib.pyplot as plt

# Sample data for the heatmap
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# Create a heatmap using seaborn
sns.set()  # Set seaborn style
sns.heatmap(data, annot=True, cmap='YlGnBu', fmt='g')  # annot=True to display the values, cmap for color map, fmt='g' for number formatting

# Add labels to the heatmap
plt.xlabel('X-Axis Label')
plt.ylabel('Y-Axis Label')
plt.title('Heatmap Example')

# Show the heatmap
plt.show()

