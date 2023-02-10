import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('imag1.1.jpg')
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = hsv_img[:,:,0], hsv_img[:,:,1], hsv_img[:,:,2]
clahe = cv2.createCLAHE(clipLimit = 15.0, tileGridSize = (20,20))
v = clahe.apply(v)

hsv_img = np.dstack((h,s,v))

rgb = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
plt.imshow(rgb);