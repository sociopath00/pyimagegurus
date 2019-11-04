"""
	@author: Akshay Nevrekar
	@created on: 20/10/2019
"""

# import necessary packages
import cv2
import imutils


image = cv2.imread("images/tictactoe.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# find contours on the board
cnts = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for i,c in enumerate(cnts):
	# compute the area of the contour along with the bounding box
	# to compute the aspect ratio
	area = cv2.contourArea(c)
	(x,y,w,h) = cv2.boundingRect(c)

	# compute the convex hull of the contour, then use the area of the
	# original contour and the area of the convex hull to compute the
	# solidity
	hull = cv2.convexHull(c)
	hullArea = cv2.contourArea(hull)
	solidity = area / float(hullArea)

	char = "?"

	if solidity > 0.9:
		char = "O"
	elif solidity > 0.5:
		char = "X"

	if char != "?":
		cv2.drawContours(image, [c], -1, (0,255,0), 3)
		# cv2.putText(image, char, (x,y,-10), cv2.FONT_HERSHEY_COMPLEX, 1.25, (0,255,0), 4)
		cv2.putText(image, char,  (x,y-10), cv2.FONT_HERSHEY_SIMPLEX,1, (0,255,0),4)

	print("{} (contour #{} -- solidity={:2f}".format(char, i+1, solidity))

cv2.imshow("Output", image)
cv2.waitKey(0)