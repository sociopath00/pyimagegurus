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
white = (255,255,255)

# draw line
cv2.line(canvas, pt1=(0,0), pt2=(300,300), color=green)

# draw another line
cv2.line(canvas, (300,0), (0,300), red, 3)
# cv2.imshow("Line", canvas)

# draw rectangle
cv2.rectangle(canvas, (10,10), (60,60), green)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)


cv2.rectangle(canvas, (50,200), (200,225), red, 5)

cv2.rectangle(canvas, (200,50),(225,125), blue, -1)   # -1 to fill it with color
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# reset our canvas and draw a white circle at the center of the canvas with
# increasing radii - from 25 pixels to 150 pixels
canvas = np.zeros((300,300,3), dtype="uint8")

(cX, cY) = (canvas.shape[1]//2, canvas.shape[0]//2)
for r in range(0,175,25):
	cv2.circle(canvas, (cX, cY), r, white)

cv2.imshow("canvas2", canvas)
cv2.waitKey(0)

# let's go crazy and draw 25 random circles
for i in range(0, 25):
	# randomly generate a radius size between 5 and 200, generate a random
	# color, and then pick a random point on our canvas where the circle
	# will be drawn
	radius = np.random.randint(5, high=200)
	color = np.random.randint(0, high=256, size=(3,)).tolist()
	pt = np.random.randint(0, high=300, size=(2,))

	# draw our random circle
	cv2.circle(canvas, tuple(pt), radius, color, -1)

# Show our masterpiece
cv2.imshow("Canvas3", canvas)
cv2.waitKey(0)

# load the image of Adrian in Florida
image = cv2.imread(IMAGE)

# draw a circle around my face, two filled in circles covering my eyes, and
# a rectangle surrounding my mouth
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

# show the output image
cv2.imshow("Output", image)
cv2.waitKey(0)
