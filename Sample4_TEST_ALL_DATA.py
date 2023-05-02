import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

# files=os.listdir('./data1/disp_noc_0')
Path0 = "C:/Users/15868/Desktop/Stereo/code/sample_code/t1/left"
Path1 = "C:/Users/15868/Desktop/Stereo/code/sample_code/t1/right"
Path2 = "C:/Users/15868/Desktop/Stereo/code/sample_code/t1/result/"
files=os.listdir(Path0)
print(files)


window_size = 10
stereo_1 = cv2.StereoBM_create(numDisparities=64, blockSize=15)

# stereo_1 = cv2.StereoSGBM_create(minDisparity = 1,
#                                    numDisparities = 64,
#                                    blockSize = window_size,
#                                    P1 = 8 * 3 * window_size * window_size,
#                                    P2 = 32 * 3 * window_size * window_size,
#                                    disp12MaxDiff = -1,
#                                    preFilterCap = 1,
#                                    uniquenessRatio = 10,
#                                    speckleWindowSize = 100,
#                                    speckleRange = 100,
#                                    mode = cv2.STEREO_SGBM_MODE_HH)

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
# mean, std = np.mean(gray), np.std(gray)
# PSNR = 20 * np.log10(255 / np.sqrt(mean))
for i in range(len(files)):
        pl = Path0 +"/" +str(files[i])
        pr = Path1 +"/" +str(files[i])
        # print(pl)
        Image1 = cv2.imread(pl)
        Image2 = cv2.imread(pr)
        print(pl)
        Ig1 = Image1[:,:,1]
        Ig2 = Image2[:, :, 1]
        disparity1 = stereo_1.compute(np.uint8(Ig1), np.uint8(Ig2))
        disparity2 = stereo_3.compute(np.uint8(Ig1), np.uint8(Ig2))
        mean, std = np.mean(disparity1), np.std(disparity1)
        PSNR = 20 * np.log10(255 / np.sqrt(mean))

        print("PSNR:",PSNR)
        name1 = "BM"
        name2 = "SGBM"
        name3 = "Original"
        name1 = name1 +"_" + str(i) +".jpg"
        name2 = name2 +"_" + str(i) +".jpg"
        name3 = name3 + "_" + str(i) + ".jpg"
        r1 = Path2 + name1
        r2 = Path2 + name2
        r3 = Path2 + name3
        cv2.imwrite(r1, disparity1)
        cv2.imwrite(r2, disparity2)
        cv2.imwrite(r3, Ig1)