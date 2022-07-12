import cv2
import numpy as np

img = cv2.imread("g/g_test.jpg")
simg = cv2.resize(img, (320,240))
print(simg.shape[0])

for i in range(simg.shape[0]):
   for j in range(simg.shape[1]):
       if simg[i][j][0] < 255 and simg[i][j][0] < 255 and simg[i][j][0] < 255:
           simg[i][j][0] = 0
           simg[i][j][1] = 0
           simg[i][j][2] = 0
cv2.imshow('image', simg)
