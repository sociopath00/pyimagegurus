"""
	@author: Akshay Nevrekar
	@created on: 26-9-2019
"""

# import necessary packages
import numpy as np
import cv2
from config import IMAGE


# read the image
image = cv2.imread(IMAGE)

# check height, width and channels
print("Width: {} pixels".format(image.shape[1]))
print("Height: {} pixels".format(image.shape[0]))
print("Channel: {}".format(image.shape[2]))

# display the image
cv2.imshow("Image", image)
cv2.waitKey(0)    # wait till key is pressed

# write the image in jpg
cv2.imwrite("images/image.jpg", image)
