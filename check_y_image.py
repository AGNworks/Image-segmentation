import cv2
import numpy as np
import os
import datetime

x = datetime.datetime.now()
with open ("about/{}_report.txt".format(x.strftime("%d_%m_%y__%H_%M")), "w") as report:
   report.write("Checking the images, if they contains just black and white pixels\n\n")

correct_imgs = 0

files = os.listdir("y\\")
print("Number of files in dir: {}".format(len(files)))

with open ("about/{}_report.txt".format(x.strftime("%d_%m_%y__%H_%M")), "a") as report:
         report.write("Total number of files in dir: {} pcs \n\nWrong pictures:\n\n".format(str(len(files))))
         
for file in files:
   img = cv2.imread("y/{}".format(str(file)))
   #print("{} : {} shape".format(file, img.shape))

   pix_numb = int(img.shape[0]) * int(img.shape[1])
   #print("Number of pixels: {}".format(pix_numb))

   #print(img[100])

   white_pixs = 0
   black_pixs = 0
   for i in range(img.shape[0]):
      for j in range(img.shape[1]):
          if img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255:
              white_pixs +=1
          elif img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0:
               black_pixs +=1
               
   if (white_pixs + black_pixs) == pix_numb:
      correct_imgs +=1
   else:
      with open ("about/{}_report.txt".format(x.strftime("%d_%m_%y__%H_%M")), "a") as report:
         report.write("{} \n".format(str(file)))

   #print("White: {}".format(white_pixs))
   #print("Black: {}".format(black_pixs))
   #print("All: {}".format(white_pixs+black_pixs))
   
print("Correct ones: {}".format(correct_imgs))

with open ("about/{}_report.txt".format(x.strftime("%d_%m_%y__%H_%M")), "a") as report:
         report.write("Correct images: {} pcs \n\n".format(str(correct_imgs)))
