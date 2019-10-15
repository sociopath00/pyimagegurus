"""
	@author: Akshay Nevrekar
	@created on: 14/10/2019
"""

import argparse
import cv2
import imutils
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)

# find the contours and grab
cnts = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# create a copy of OG image and draw contours on it
clone = image.copy()
cv2.drawContours(clone, cnts, -1, (0,255,0), 2)

print(f"Found {len(cnts)} contours in image")

cv2.imshow("Contours", clone)
cv2.waitKey(0)

# reconstruct the image
clone = image.copy()
cv2.destroyAllWindows()

for (i,c) in enumerate(cnts, start=1):
	print(f"Drawing contour #{i} ")
	cv2.drawContours(clone, [c], -1, (0,255,0), 2)
	cv2.imshow("Single contour",clone)
	cv2.waitKey(0)

# re-clone the image and close all open windows
clone = image.copy()
cv2.destroyAllWindows()

# find contours in the image, but this time keep only the EXTERNAL
# contours in the image
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cv2.drawContours(clone, cnts, -1, (0, 255, 0), 2)
print(f"Found {len(cnts)} EXTERNAL contours")

# show the output image
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

clone = image.copy()
cv2.destroyAllWindows()

# loop over the contours individually
for c in cnts:
	# construct a mask by drawing only the current contour
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)

	# show the images
	cv2.imshow("Image", image)
	cv2.imshow("Mask", mask)
	cv2.imshow("Image + Mask", cv2.bitwise_and(image, image, mask=mask))
	cv2.waitKey(0)