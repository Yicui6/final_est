import numpy as np
import cv2
import camera_configs


cv2.namedWindow("left")
cv2.namedWindow("right")
cv2.namedWindow("depth")
cv2.moveWindow("left", 0, 0)
cv2.moveWindow("right", 600, 0)
cv2.createTrackbar("num", "depth", 0, 10, lambda x: None)
cv2.createTrackbar("blockSize", "depth", 5, 255, lambda x: None)
# camera1 = cv2.VideoCapture(0)
# camera2 = cv2.VideoCapture(1)

# 添加点击事件，打印当前点的距离
def callbackFunc(e, x, y, f, p):
    if e == cv2.EVENT_LBUTTONDOWN:
        print (threeD[y][x] )
        print ("Distance unit is mm")

cv2.setMouseCallback("depth", callbackFunc, None)

while True:
#     ret1, frame1 = camera1.read()
#     ret2, frame2 = camera2.read()
    frame1 = cv2.imread("./left_shot_13.png")
    frame2 = cv2.imread("./right_shot_13.png")

    # if not ret1 or not ret2:
        # break

    # 根据更正map对图片进行重构
    img1_rectified = cv2.remap(frame1, camera_configs.left_map1, camera_configs.left_map2, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(frame2, camera_configs.right_map1, camera_configs.right_map2, cv2.INTER_LINEAR)

    # 将图片置为灰度图，为StereoBM作准备
    # imgL = cv2.cvtColor(img1_rectified, cv2.COLOR_BGR2GRAY)
    # imgR = cv2.cvtColor(img2_rectified, cv2.COLOR_BGR2GRAY)

    imgL = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    imgR = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # imgL = cv2.GaussianBlur(imgL, (5, 5), 0)
    # imgR = cv2.GaussianBlur(imgR, (5, 5), 0)
    # 两个trackbar用来调节不同的参数查看效果
    num = cv2.getTrackbarPos("num", "depth")
    blockSize = cv2.getTrackbarPos("blockSize", "depth")
    if blockSize % 2 == 0:
        blockSize += 1
    if blockSize < 5:
        blockSize = 5

    # 根据Block Maching方法生成差异图（opencv里也提供了SGBM/Semi-Global Block Matching算法，有兴趣可以试试）
    # stereo = cv2.StereoBM_create(numDisparities=16*num, blockSize=blockSize)

    stereo = cv2.StereoSGBM_create(
            minDisparity=-1,
            numDisparities=16*num+16,  # max_disp has to be dividable by 16 f. E. HH 192, 256
            blockSize=blockSize,
            P1=8 * 3 * blockSize,
            # wsize default 3; 5; 7 for SGBM reduced size image; 15 for SGBM full size image (1300px and above); 5 Works nicely
            P2=32 * 3 * blockSize,
            disp12MaxDiff=12,
            uniquenessRatio=10,
            speckleWindowSize=50,
            speckleRange=32,
            preFilterCap=63,
            mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY
        )

    disparity = stereo.compute(imgL, imgR)

    disp = cv2.normalize(disparity, disparity, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    threeD = cv2.reprojectImageTo3D(disparity.astype(np.float32)/16., camera_configs.Q)
    img_color = cv2.applyColorMap(cv2.convertScaleAbs(disp, alpha=7), cv2.COLORMAP_JET)

    cv2.imshow("left", img1_rectified)
    cv2.imshow("right", img2_rectified)

    cv2.imshow("left", imgL)
    cv2.imshow("right", imgR)
    cv2.imshow("depth", disp)
    cv2.imshow("depth_color", img_color)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    elif key == ord("s"):
        cv2.imwrite("./BM_left.jpg", imgL)
        cv2.imwrite("./BM_right.jpg", imgR)
        cv2.imwrite("./BM_depth.jpg", disp)

# camera1.release()
# camera2.release()
cv2.destroyAllWindows()