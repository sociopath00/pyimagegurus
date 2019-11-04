"""
	@author: Akshay Nevrekar
	@created on: 25/10/2019
"""

import cv2
import imutils


# image = cv2.imread("images/receipt.png")
image = cv2.imread("images/dog_contour.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("Original", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:7]

for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.1*peri, True)
	print("original: {}, approx: {}".format(len(c), len(approx)))

	if len(approx)==4:
		cv2.drawContours(image, [approx], -1, (0,255,0), 2)

cv2.imshow("Output", image)
cv2.waitKey(0)
