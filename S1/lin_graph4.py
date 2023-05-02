import matplotlib.pyplot as plt

# Data
x = ['Point 1', 'Point 2', 'Point 3', 'Point 4', 'Point 5', 'Point 6', 'Point 7', 'Point 8', 'Point 9']
BM = [778.70, 768.17, 864.28, 727.03, 821.03, 697.13, 762.95, 773.24, 757.06]
SGBM = [806.13, 820.18, 793.67, 800.7, 804.5, 890.2, 750.3, 803.6, 820.3]
plt.figure(figsize=(12, 6), dpi=500)
# Create a line graph with two lines
plt.plot(x, BM, label='BM', color='blue')
plt.plot(x, SGBM, label='SGBM', color='red')

# Add the horizontal line called "Exact Distance" with a value of 800
plt.axhline(y=800, label='Exact Distance (800 mm)', color='green', linestyle='--')

# Add labels and title
plt.xlabel('Points')
plt.ylabel('Values (mm)')
plt.title('Base-Case(No Attack)')

# Set custom y-axis ticks
plt.yticks([-8000,  800, 5000])

# Add a legend
plt.legend()

# Show the plot
plt.show()
