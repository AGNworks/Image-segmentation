import cv2
import numpy as np

img = cv2.imread("x/x_test.jpg")
simg = cv2.resize(img, (320,240))
print(simg.shape)

cv2.imwrite("x/x_1.jpg", simg)
