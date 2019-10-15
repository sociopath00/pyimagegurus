"""
	@author: Akshay Nevrekar
	@created on: 13/10/2019
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)

cv2.imshow("gray", gray)
cv2.imshow("blurred", blurred)

wide = cv2.Canny(blurred, 10, 200)
mid = cv2.Canny(blurred, 30, 150)
tight = cv2.Canny(blurred, 240, 250)

cv2.imshow("Wide edge map", wide)
cv2.imshow("Mid Edge map", mid)
cv2.imshow("tight Edge map", tight)
cv2.waitKey(0)
