# Python code for Corrosion Detection

import numpy as np
import cv2


# read and capturing image
img = cv2.imread("tank2.jpeg", cv2.IMREAD_COLOR)

# Convert the imageFrame in
# BGR(RGB color space) to
# HSV(hue-saturation-value)
# color space
hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Set range for corrosion color and
# define mask
corr_lower = np.array([0, 70, 70], np.uint8)
corr_upper = np.array([20, 200, 150], np.uint8)
corr_mask = cv2.inRange(hsvFrame, corr_lower, corr_upper)
	
# Morphological Transform, Dilation
# for each corrosion color and bitwise_and operator
# between imageFrame and mask determines
# to detect only that particular corrosion color
kernal = np.ones((5, 5), "uint8")
	
# For corrosion color
corr_mask = cv2.dilate(corr_mask, kernal)
res_corr = cv2.bitwise_and(img, img,
						mask = corr_mask)

# Creating contour to track corrosion color
contours, hierarchy = cv2.findContours(corr_mask,
									cv2.RETR_TREE,
									cv2.CHAIN_APPROX_SIMPLE)
	
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    if(area > 300):
        x, y, w, h = cv2.boundingRect(contour)
        imageFrame = cv2.rectangle(img, (x, y),
                                (x + w, y + h),
                                (0, 0, 255), 2)
        
        cv2.putText(img, "Corrosion", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))	
			
# Program Termination
cv2.imshow("Corrosion Detection", cv2.resize(img, (1000, 800)))
cv2.waitKey(0)
cv2.destroyAllWindows()