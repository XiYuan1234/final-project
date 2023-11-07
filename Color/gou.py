import cv2
import numpy as np
img = cv2.imread('gou.jpg',0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
cv2.imwrite("1" + '.jpg', erosion)
dilation = cv2.dilate(img ,kernel,iterations = 1)
cv2.imwrite("2" + '.jpg', dilation)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite("3" + '.jpg', opening)