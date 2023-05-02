import matplotlib.pyplot as plt

# Data
x = ['Point 1', 'Point 2', 'Point 3', 'Point 4', 'Point 5', 'Point 6', 'Point 7', 'Point 8', 'Point 9']
setting_1 = [954.38, 912.02, 884.52, -630.17, -630.09, 912.02, 854.28, 900.78, 912.67]
setting_2 = [954.37, 933.03, 870.99, 918.98, 1005.56, 1028.11, 976.07, 947.22, 870.99]
plt.figure(figsize=(12, 6), dpi=500)
# Create a line graph with three lines
plt.plot(x, setting_1, label='Setting 1', color='blue')
plt.plot(x, setting_2, label='Setting 2', color='red')

# Add the horizontal line called "Exact Distance" with a value of 914
plt.axhline(y=914, label='Exact Distance  (914 mm)', color='green', linestyle='--')

# Add labels and title
plt.xlabel('Points')
plt.ylabel('Values (mm)')
plt.title('BM Alg Result')
plt.yticks([700,  914, 1100])
# Add a legend
plt.legend()

# Show the plot
plt.show()
