# import cv2
# import numpy as np

import numpy as np
import cv2 as cv2
import os

path = "C://Users/saurabh shukla/Desktop/IDEX Project/Output2 Clahe+Blur"
# img = cv2.imread("reInput1.jpg")
# image = cv2.resize(img, (400,300))
# # image = cv2.imread("imag1.jpg", cv2.IMREAD_COLOR)

# gaussian_blur = cv2.GaussianBlur(image, (7,7), 2)

# sharpend1 = cv2.addWeighted(image, 1.5, gaussian_blur, -0.5, 0)
# sharpend2 = cv2.addWeighted(image, 3.5, gaussian_blur, -2.5, 0)
# sharpend3 = cv2.addWeighted(image, 7.5, gaussian_blur, -6.5, 0)

# cv2.imshow("sharpend1", sharpend1)
# cv2.imshow("sharpend3", sharpend3)
# cv2.imshow("sharpend2", sharpend2)
# cv2.imshow("original", image)
# cv2.waitKey(0)

img = cv2.imread("reInput1.jpg")
image = cv2.resize(img, (400,300))
# image = cv2.imread("imag1.jpg", cv2.IMREAD_COLOR)

gaussian_blur = cv2.GaussianBlur(image, (7,7), 2)

# sharpend1 = cv2.addWeighted(image, 1.5, gaussian_blur, -0.5, 0)
sharpend2 = cv2.addWeighted(image, 3.5, gaussian_blur, -2.5, 0)
# sharpend3 = cv2.addWeighted(image, 7.5, gaussian_blur, -6.5, 0)

cv2.imwrite("opt1.jpg",sharpend2)

# cv2.imshow("sharpend1", sharpend1)
# cv2.imshow("sharpend3", sharpend3)
# cv2.imshow("sharpend2", sharpend2)
# cv2.imshow("original", image)


img = cv2.imread("opt1.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)

#configure CLAHE
clahe = cv2.createCLAHE(clipLimit=10,tileGridSize=(8,8))

#0 to 'L' channel, 1 to 'a' channel, and 2 to 'b' channel
img[:,:,0] = clahe.apply(img[:,:,0])

img = cv2.cvtColor(img, cv2.COLOR_Lab2RGB)

cv2.imshow("image", img)
cv2.imwrite(os.path.join(path,"1.jpg"),img)
cv2.waitKey(0)