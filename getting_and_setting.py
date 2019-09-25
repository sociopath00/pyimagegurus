"""
	@author: Akshay Nevrekar
	@created on: 26/09/2019
"""

# import necessary packages
from config import IMAGE
import cv2
import numpy as np


# read image
image = cv2.imread(IMAGE)

# get height and width
(h,w) = image.shape[:2]

# display original image
cv2.imshow("original image", image)
cv2.waitKey(500)

# get pixel values at location (0,0)
bgr = image[0,0]
print("Pixel at (0,0): Blue {}, Green {}, Red {}".format(*bgr))

# let's change value of pixel at (0,0) and make it red
image[0,0] = (0,0,255)
print("Pixel at (0,0): Blue {}, Green {}, Red {}".format(*bgr))

# get the center of an image
(cX, cY) = (w//2, h//2)

# get top left corner of an image
tl = image[0:cY, 0:cX]
cv2.imshow("Top Left Corner", tl)

# get top right corner of an image
tr = image[0:cY, cX:]
cv2.imshow("Top Right Corner", tr)

# get bottom left corner
bl = image[cY:, 0:cX]
cv2.imshow("Bottom left Corner", bl)

# get bottom right corner
br = image[cY:, cX:]
cv2.imshow("Bottom right Corner", br)

# fill top left corner with Green color
image[0:cY, 0:cX] = (0,255,0)
cv2.imshow("Updated Image", image)
cv2.waitKey(0)
