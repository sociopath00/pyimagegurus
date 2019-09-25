"""
	@author: Akshay Nevrekar
	@created on: 26-9-2019
"""

# import necessary packages
import numpy as np
import cv2
from config import IMAGE


# read image
image = cv2.imread(IMAGE)

# initialize our canvas as a 300x300 with 3 channels, Red, Green,
# and Blue, with a black background
canvas = np.zeros((300,300,3), dtype="uint8")

# initialize color tuples
green = (0,255,0)
blue = (255,0,0)
red = (0,0,255)

# draw line
cv2.line(canvas, pt1=(0,0), pt2=(300,300), color=green)

# draw another line
cv2.line(canvas, (300,0), (0,300), red, 3)

cv2.imshow("Line", canvas)
cv2.waitKey(0)


