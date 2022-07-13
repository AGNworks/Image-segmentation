import cv2
import numpy as np
import os

files = os.listdir("g\\")
print("Number of files in dir: {}".format(len(files)))

for file in files:
    img = cv2.imread("g/{}".format(str(file)))
    print(img.shape)
    counter = 0
    for i in range(img.shape[0]):
       for j in range(img.shape[1]):
           counter += 1
           if img[i][j][0] >= 254 and img[i][j][1] >= 254 and img[i][j][2] >= 254:
               img[i][j][0] = 255
               img[i][j][1] = 255
               img[i][j][2] = 255
           else:
               img[i][j][0] = 0
               img[i][j][1] = 0
               img[i][j][2] = 0

    print(counter)
    cv2.imwrite("y/y_{}".format(str(file)), img) #using jpg made problems(RGB values changed at saving)
