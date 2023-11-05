import seaborn as sns
import matplotlib.pyplot as plt

# Sample data for the heatmap (limited to the period from 2015 to 2023)
years = list(range(2015, 2024))  # Years from 2015 to 2023
data = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],  # Data for 2015
    [10, 11, 12, 13, 14, 15, 16, 17, 18],  # Data for 2016
    [19, 20, 21, 22, 23, 24, 25, 26, 27],  # Data for 2017
    [28, 29, 30, 31, 32, 33, 34, 35, 36],  # Data for 2018
    [37, 38, 39, 40, 41, 42, 43, 44, 45],  # Data for 2019
    [46, 47, 48, 49, 50, 51, 52, 53, 54],  # Data for 2020
    [55, 56, 57, 58, 59, 60, 61, 62, 63],  # Data for 2021
    [64, 65, 66, 67, 68, 69, 70, 71, 72],  # Data for 2022
    [73, 74, 75, 76, 77, 78, 79, 80, 81]   # Data for 2023
]

# Create a heatmap using seaborn
sns.set()  # Set seaborn style
sns.heatmap(data, annot=True, cmap='YlGnBu', fmt='g', xticklabels=years, yticklabels=years)  
# annot=True to display the values, cmap for color map, fmt='g' for number formatting
# xticklabels and yticklabels to set the labels for x and y axes

# Add labels to the heatmap
plt.xlabel('Years')
plt.ylabel('Years')
plt.title('Heatmap Example (2015-2023)')

# Show the heatmap
plt.show()
