## Sample1: RealSense Camera take images

This Python program uses the [pyrealsense2](https://pypi.org/project/pyrealsense2/) library to interface with a [RealSense](https://www.intelrealsense.com/) depth camera and display the color, depth, and infrared image streams using [OpenCV](https://opencv.org/). It also allows the user to capture snapshots of the camera's output by pressing the 't' key.

## Configuration

The program first configures the RealSense camera by creating a pipeline and enabling the color, infrared, and depth streams with a resolution of 848x480 and a frame rate of 15 frames per second.

## Alignment

The program then creates an align object using `rs.align` to align the depth frames with the color frames.

## Image Processing and Display

Inside the main loop, the program waits for frames from the RealSense camera and processes them using the align object to obtain aligned frames. The aligned frames are then converted into numpy arrays, which are used to display the color, depth, and infrared images using OpenCV.

## Snapshot

The program allows the user to capture a snapshot of the current camera output by pressing the 't' key. When the 't' key is pressed, the program saves the current color, depth, and infrared images as well as the depth_colormap and depth_frame to the specified folder with a unique filename. The filename is constructed using the current snapshot counter, which is incremented every time a new snapshot is taken.

## Exiting the Program

The program displays the camera output until the user presses the 'ESC' key. When the 'ESC' key is pressed, the program stops streaming from the RealSense camera and closes all OpenCV windows.

# RealSense Camera with OpenCV and Pointcloud

This Python program uses the [pyrealsense2](https://pypi.org/project/pyrealsense2/) library to interface with a [RealSense](https://www.intelrealsense.com/) depth camera and display the color and depth image streams using [OpenCV](https://opencv.org/). It also allows the user to calculate and display the pointcloud of the scene.

## Configuration

The program first configures the RealSense camera by creating a pipeline and enabling the color and depth streams with a resolution of 640x480 and a frame rate of 15 frames per second.

## Alignment

The program then creates an align object using `rs.align` to align the depth frames with the color frames.

## Pointcloud Generation

The program generates a pointcloud object and calculates the points and texture coordinates using `rs.points` and `rs.pointcloud.calculate`, respectively. The generated pointcloud is then converted into numpy arrays, which are used to display the scene's pointcloud and corresponding color image using OpenCV.

## Image Processing and Display

Inside the main loop, the program waits for frames from the RealSense camera and processes them using the align object to obtain aligned frames. The aligned frames are then converted into numpy arrays, which are used to display the color and depth images using OpenCV. Additionally, the program calculates and displays the distance and 3D coordinates of a selected pixel in the scene.

## Exiting the Program

The program displays the camera output until the user presses the 'ESC' key. When the 'ESC' key is pressed, the program stops streaming from the RealSense camera and closes all OpenCV windows.







## Sample2: # RealSense Camera LED Tracking with OpenCV

This Python program uses the [pyrealsense2](https://pypi.org/project/pyrealsense2/) library to interface with a [RealSense](https://www.intelrealsense.com/) depth camera and display the color and depth image streams using [OpenCV](https://opencv.org/). It also allows the user to track the LED lights by tuning the color thresholds with the help of trackbars. 

## Trackbar Configuration

The program creates trackbars for adjusting the color thresholds for the red LED. These trackbars are used to fine-tune the lower and upper bounds for hue, saturation, and value (HSV) color channels. The program also creates trackbars for adjusting the morphological operations such as opening, closing, eroding, and dilating.

## Image Processing and Display

Inside the `led_practice()` function, the program waits for frames from the RealSense camera and processes them using the align object to obtain aligned frames. The aligned frames are then converted into numpy arrays, which are used to display the color and depth images using OpenCV. 

The program then performs the following operations on the color image:
- Converts the color image from BGR to HSV color space
- Applies a mask to the color image using the tuned color thresholds for the red LED
- Displays the resulting image with the tracked LED light and the distance to the camera in centimeters
- Displays the coordinates of the LED light in the X, Y, and Z axes

The program also calculates the depth of the LED light using the pointcloud object and displays the resulting depth value in the console.

## Exiting the Program

The program displays the camera output until the user presses the 'ESC' key. When the 'ESC' key is pressed, the program stops streaming from the RealSense camera and closes all OpenCV windows.




## sample3 # RUNNINg for detail Careful parameter adjustment test

This Python program uses OpenCV and Matplotlib libraries to perform stereo matching on a pair of left and right images to generate the corresponding disparity maps. The program then displays the generated disparity maps and saves them as JPEG files.

## Program Description

### Step 1: Import Libraries

The first step in the program is to import the required libraries, which are `cv2` for OpenCV and `matplotlib` for Matplotlib.

### Step 2: Load Left and Right Images

The program then loads the left and right images from their respective file paths using the `cv2.imread()` function. The images are loaded in grayscale format by passing the parameter `0` to the function.

### Step 3: Define Stereo Matching Parameters

The program defines the stereo matching parameters for three different stereo matching algorithms:

- **StereoBM**: It uses block matching algorithm to calculate the disparity map. The algorithm takes two mandatory parameters - `numDisparities` and `blockSize`.
- **StereoSGBM**: It is another block matching algorithm and includes additional parameters that provide more flexibility and control over the disparity map calculation. The algorithm takes several parameters like `numDisparities`, `blockSize`, `P1`, `P2`, `speckleWindowSize`, `uniquenessRatio`, etc.
- **StereoSGBM with tuned parameters**: This algorithm is the same as the previous algorithm but with some tuned parameters for better results.

### Step 4: Calculate Disparity Maps

The program then calculates the disparity maps using the `compute()` function of the `cv2.StereoBM_create()` and `cv2.StereoSGBM_create()` classes, respectively. The disparity maps generated by each algorithm are saved as JPEG files.

### Step 5: Display and Save Disparity Maps

Finally, the program uses Matplotlib to display the generated disparity maps in a 2x2 grid. The images are loaded using `cv2.imread()` function and displayed using the `plt.imshow()` function. The `plt.axis()` function is used to turn off the axes of the images. The `plt.title()` function is used to set the titles of the images.

The generated disparity maps are also saved as JPEG files using the `cv2.imwrite()` function.

## Conclusion

This Python program demonstrates how to perform stereo matching using OpenCV and Matplotlib libraries. The program calculates disparity maps using three different stereo matching algorithms and displays the generated disparity maps in a 2x2 grid.



## Sample4:# running for Datasets TEST

This Python program performs stereo matching using two different algorithms, Block Matching (BM) and Semi-Global Block Matching (SGBM), on a pair of left and right images. The program reads in left and right images from the specified paths and computes the disparity maps using the two algorithms. 

The program uses OpenCV's built-in `cv2.StereoBM_create` and `cv2.StereoSGBM_create` functions to create two stereo matcher objects. Both stereo matchers are set up with a window size of 10 and other relevant parameters such as the number of disparities, block size, and P1 and P2 values.

The program iterates through all the image files in the specified directory and reads each pair of left and right images. The green channel of the images is extracted, and the disparity maps are computed using both BM and SGBM algorithms. The mean and standard deviation of the first disparity map are calculated and used to compute the Peak Signal-to-Noise Ratio (PSNR).

The program saves the resulting disparity maps and the original left image to the specified directory using the names "BM_{i}.jpg", "SGBM_{i}.jpg", and "Original_{i}.jpg", where i is the index of the current image in the list of image files. The PSNR value is printed for each image.

Note that the program contains commented-out code for another SGBM algorithm with different parameter values, which can be used by uncommenting it and commenting out the other SGBM algorithm.

## In the S1,S2,S3 Folders, which are three test  scenarios， each has their test image took by Real Sece and basd on the test, the value (distence ) - 1500 mm is the real distence

## Description of the Stereo Depth Sensing Program

This Python program performs stereo depth sensing using two images from a stereo camera system. The program reads in the left and right images from the specified paths and rectifies them using the camera calibration parameters stored in the `camera_configs` module.

The program then converts the rectified left and right images to grayscale and applies a trackbar to adjust the parameters for the StereoSGBM algorithm used for computing the disparity map. The algorithm generates a disparity map by calculating the difference between the left and right images.

The program normalizes the disparity map and then projects it to a 3D space using the Q matrix from the calibration parameters. The 3D space represents the distance of each pixel from the stereo camera system.

The program displays the rectified left and right images, the disparity map, and a color-coded depth map. The user can click on any pixel in the depth map to print the corresponding distance in millimeters.

The program can be exited by pressing the "q" key or the user can save the images by pressing the "s" key. 

Note that the program uses commented-out code for another algorithm called StereoBM, which can be used by commenting out the SGBM code and uncommenting the StereoBM code.


