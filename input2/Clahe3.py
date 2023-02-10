import numpy as np
import cv2 as cv2
import os

path = "C://Users/saurabh shukla/Desktop/IDEX Project/Output clahe"

img = cv2.imread("input4.jpg", cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)

#configure CLAHE
clahe = cv2.createCLAHE(clipLimit=10,tileGridSize=(8,8))

#0 to 'L' channel, 1 to 'a' channel, and 2 to 'b' channel
img[:,:,0] = clahe.apply(img[:,:,0])

img = cv2.cvtColor(img, cv2.COLOR_Lab2RGB)

cv2.imshow("image", img)
cv2.imwrite(os.path.join(path,"4.jpg"),img)
cv2.waitKey(0)
cv2.destroyAllWindows()