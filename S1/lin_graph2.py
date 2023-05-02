import matplotlib.pyplot as plt

# Data
x = ['Point 1', 'Point 2', 'Point 3', 'Point 4', 'Point 5', 'Point 6', 'Point 7', 'Point 8', 'Point 9']
setting_1 = [1005.56, 933.03, 864.28, 933.03, 951.03, 954.37, 894.73, 857.60, 857.60]
setting_2 = [1068.80, 977.74, 964.28, 950.96, 1061.57, 957.60, 1068.80, 924.73, 1105.56]
plt.figure(figsize=(12, 6), dpi=500)
# Create a line graph with three lines
plt.plot(x, setting_1, label='Setting 1', color='blue')
plt.plot(x, setting_2, label='Setting 2', color='red')

# Add the horizontal line called "Exact Distance" with a value of 914
plt.axhline(y=914, label='Exact Distance (914 mm)', color='green', linestyle='--')

# Add labels and title
plt.xlabel('Points')
plt.ylabel('Values (mm)')
plt.title('SGBM Alg Result')
plt.yticks([700,  914, 1100])
# Add a legend
plt.legend()

# Show the plot
plt.show()