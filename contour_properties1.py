"""
	@author: Akshay Nevrekar
	@created on: 18/10/2019
"""

# import the necessary packages
import numpy as np
import argparse
import cv2
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# read image
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find external contours in the image
cnt = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnt)

clone = image.copy()

for c in cnts:
	M = cv2.moments(c)
	cX = int(M["m10"]/M["m00"])
	cY = int(M["m01"]/M["m00"])
	cv2.circle(clone, (cX, cY), 10, (0,255,0), -1)


cv2.imshow("Centroids", clone)
cv2.waitKey(0)

clone = image.copy()

