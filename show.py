import cv2
import matplotlib.pyplot as plt


Image1 = cv2.imread('disparity1.jpg')
Image2 = cv2.imread('disparity2.jpg')
Image3 = cv2.imread('disparity3.jpg')
Image4 = cv2.imread('disparity4.jpg')
Image5 = cv2.imread('disparity5.jpg')
Image6 = cv2.imread('disparity6.jpg')
Image7 = cv2.imread('disparity7.jpg')
Image8 = cv2.imread('disparity8.jpg')
Image9 = cv2.imread('disparity9.jpg')

fig = plt.figure(figsize=(15, 8))
rows = 3
columns = 3
# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("BM: windowsize 5")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(Image2)
plt.axis('off')
plt.title("SGBM: windowsize 5")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(Image3)
plt.axis('off')
plt.title("3WAY_SGBM with careful setup : windowsize 5")

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)

# showing image
plt.imshow(Image4)
plt.axis('off')
plt.title("BM: windowsize 10")

fig.add_subplot(rows, columns, 5)
plt.imshow(Image5)
plt.axis('off')
plt.title("SGBM: windowsize 10")

fig.add_subplot(rows, columns, 6)
plt.imshow(Image6)
plt.axis('off')
plt.title("3WAY_SGBM with careful setup : windowsize 10")

fig.add_subplot(rows, columns, 7)
plt.imshow(Image7)
plt.axis('off')
plt.title("BM: windowsize 15")

fig.add_subplot(rows, columns, 8)
plt.imshow(Image8)
plt.axis('off')
plt.title("SGBM: windowsize 15")

fig.add_subplot(rows, columns, 9)
plt.imshow(Image9)
plt.axis('off')
plt.title("3WAY_SGBM with careful setup : windowsize 15")


plt.show()