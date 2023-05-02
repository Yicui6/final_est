import cv2
import matplotlib.pyplot as plt



# bm = cv2.StereoSGBM('MinDisparity',0,'numDisparities',16,'blockSize',3,'P1',0,'P2',0, 'disp12MaxDiff',0,'preFilterCap',0,'uniquenessRatio',0, 'speckleWindowSize',0,'speckleRange',0,'mode', )
left_1 = cv2.imread("./camera_shot/left_shot_0.png",0)
right_1 = cv2.imread("./camera_shot/right_shot_0.png",0)
# cv2.imshow("Input", right)
# cv2.imshow("Input", left)
# plt.imshow(left)

stereo_1 = cv2.StereoBM_create(numDisparities=16, blockSize=15)
stereo_2 = cv2.StereoSGBM_create(numDisparities=16, blockSize=15)
window_size = 15
stereo_3 = cv2.StereoSGBM_create(
        minDisparity=-1,
        numDisparities=5*16,  # max_disp has to be dividable by 16 f. E. HH 192, 256
        blockSize=window_size,
        P1=8 * 3 * window_size,
        # wsize default 3; 5; 7 for SGBM reduced size image; 15 for SGBM full size image (1300px and above); 5 Works nicely
        P2=32 * 3 * window_size,
        disp12MaxDiff=12,
        uniquenessRatio=10,
        speckleWindowSize=50,
        speckleRange=32,
        preFilterCap=63,
        mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
    )



disparity1 = stereo_1.compute(left_1, right_1)
disparity2 = stereo_2.compute(left_1, right_1)
disparity3 = stereo_3.compute(left_1, right_1)

# cv2.imshow('disparity image', disparity)



plt.imshow(disparity1)
cv2.imwrite('disparity7.jpg', disparity1)
cv2.imwrite('disparity8.jpg', disparity2)
cv2.imwrite('disparity9.jpg', disparity3)
cv2.waitKey(0)

Image1 = cv2.imread('disparity1.jpg')
Image2 = cv2.imread('disparity2.jpg')
Image3 = cv2.imread('disparity3.jpg')
Image4 = cv2.imread('disparity4.jpg')
Image5 = cv2.imread('disparity5.jpg')
Image6 = cv2.imread('disparity6.jpg')
Image7 = cv2.imread('disparity7.jpg')
Image8 = cv2.imread('disparity8.jpg')
Image9 = cv2.imread('disparity9.jpg')

fig = plt.figure(figsize=(10, 7))
rows = 2
columns = 2
# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 1)

# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("First")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 2)

# showing image
plt.imshow(Image2)
plt.axis('off')
plt.title("Second")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 3)

# showing image
plt.imshow(Image3)
plt.axis('off')
plt.title("Third")

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 4)

# showing image
plt.imshow(Image4)
plt.axis('off')
plt.title("Fourth")


# f,axarr = plt.subplot(1,1)
# axarr[0].imshow('disparity7.jpg')
# axarr[1].imshow(v_slice[1])
# axarr[2].imshow(v_slice[2])
# axarr[3].imshow(v_slice[3])