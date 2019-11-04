"""
	@author: Akshay Nevrekar
	@created on: 19/10/2019
"""

import numpy as np
import cv2
import imutils


image = cv2.imread("images/shapes_example.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("original", image)
cv2.waitKey(0)

cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

clone = image.copy()

for c in cnts:
	M = cv2.moments(c)
	cX = int(M["m10"]/M["m00"])
	cY = int(M["m01"]/M["m00"])
	print("Centroids ",cX, cY)
	area = cv2.contourArea(c)
	perimeter = cv2.arcLength(c, True)
	print("Area ",area)
	print("Perimeter ", perimeter)
	cv2.circle(clone, (cX, cY), 10, (0, 255, 0), -1)