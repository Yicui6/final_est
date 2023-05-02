import matplotlib.pyplot as plt

# Data
x = ['Point 1', 'Point 2', 'Point 3', 'Point 4', 'Point 5', 'Point 6', 'Point 7', 'Point 8', 'Point 9']
BM = [752.56, -62882.5, 721.99, -62882, -62882, 663.260, -62882, -62882, 832.527]
SGBM = [781.00, 752.56, 711.98, 707.01, -62882, -62882, 747.41, 757.748, 757.748]
plt.figure(figsize=(12, 6), dpi=500)
# Create a line graph with two lines
plt.plot(x, BM, label='BM', color='blue')
plt.plot(x, SGBM, label='SGBM', color='red')

# Add the horizontal line called "Exact Distance" with a value of 800
plt.axhline(y=800, label='Exact Distance (800 mm)', color='green', linestyle='--')

# Add labels and title
plt.xlabel('Points')
plt.ylabel('Values (mm)')
plt.title('Attack Method 2 on BM and SGBM')

# Set custom y-axis ticks
plt.yticks([-8000,  800, 5000])

# Add a legend
plt.legend()

# Show the plot
plt.show()
