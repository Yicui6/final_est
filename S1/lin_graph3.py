import matplotlib.pyplot as plt

# Data
x = ['Point 1', 'Point 2', 'Point 3', 'Point 4', 'Point 5', 'Point 6', 'Point 7', 'Point 8', 'Point 9']
BM = [773.42, -32191.26, -32191.26, -32191.26, 1051.03, 1982.69, 1982.69, 2151.04, 2151.04]
SGBM = [784.01, 752.56, 711.98, 707.01, -62888, -62888, 773.427, 747.41, 757.74]
plt.figure(figsize=(12, 6), dpi=500)
# Create a line graph with three lines
plt.plot(x, BM, label='BM', color='blue')
plt.plot(x, SGBM, label='SGBM', color='red')

# Add the horizontal line called "Exact Distance" with a value of 914
# plt.axhline(y=914, label='Exact Distance (914)', color='green', linestyle='--')

# Add another horizontal line called "Exact Distance" with a value of 800
plt.axhline(y=800, label='Exact Distance (800 mm)', color='green', linestyle='--')

# Add labels and title
plt.xlabel('Points')
plt.ylabel('Values (mm)')
plt.title('Attack Method 1 on BM and SGBM')

# Set custom y-axis ticks
plt.yticks([-8000,  800, 5000])

# Add a legend
plt.legend()

# Show the plot
plt.show()
