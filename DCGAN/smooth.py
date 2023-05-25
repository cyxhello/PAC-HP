#coding:utf-8

import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

img2 = cv2.imread("white.png")

files = os.listdir('gen/2_5/')
for file in files:
    img = cv2.imread('gen/2_5/' + file)
    img_blur = cv2.blur(img, (3,3))
    res = cv2.addWeighted(img_blur, 0.8, img2, 0.2, 0)
    cv2.imwrite('gen/2_5_smooth/' + file, res)


# img = cv.imread("dummy_gen_44_2_img.png")
# img_gauss = cv.GaussianBlur(img,(3,3),1)
# # cv.imshow("img",img)
# cv.imwrite("gauss_res.png",img_gauss) 
# img_blur = cv.blur(img,(3,5))
# cv.imwrite("mean_res.png",img_blur) 

# cv.imshow("img_gauss",img_gauss)
# cv.waitKey(0)
# cv.destroyAllWindows()

# GaussianBlur()