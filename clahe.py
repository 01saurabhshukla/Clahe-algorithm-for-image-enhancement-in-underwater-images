import numpy as np
import cv2 as cv

img= cv.imread("imag1.1.jpg",0)
cv.imshow("Org",img)

cv.waitKey(0)

clahe=cv.createCLAHE(cliplimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv.imwrite("Clahe enhamced",cl1)
cv.imshow("enhanced",cl1)

cv.waitKey(0)
