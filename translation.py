"""
	@author: Akshay Nevrekar
	@date: 26/09/1991
"""

import numpy as np
import cv2
import imutils
from config import IMAGE


image = cv2.imread(IMAGE)

# NOTE: Translating (shifting) an image is given by a NumPy matrix in
# the form:  [[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y direction -- let's translate the image 25 pixels to the
# right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
# cv2.waitKey(0)

M = np.float32([[1, 0, -50], [0, 1, -90]])

shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
# cv2.waitKey(0)

# using imutils
shifted = imutils.translate(image, 25, 50)
cv2.imshow("Shifted Down and Right with imutils", shifted)
cv2.waitKey(0)
