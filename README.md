# Corrosion-Detection-with-Computer-Vision

This approach uses Python and OpenCV to track corrosion depending on its color

The technique takes an RGB picture as input. The first step is to convert the image's color space from RGB to HSV. The HSV color model is used for color identification jobs because it is more resistant to changes in environmental illumination. This property is due to the separation of the intensity-brightness (Value) information from the color information (Hue).

The following step is to establish the HSV color range that depicts corrosion by specifying a lower and higher limit for HSV values. Pixels in the image that contain these values will be retrieved and classified as corrosion. The extraction is carried out by thresholding all values inside the specified range. This produces a mask, which is a binary image in which the pixels with values in the specified color range are white and the rest are black.

A non-linear filter is employed to execute the morphological operation of dilation to cope with holes in corrosion-prone areas. The operation is mathematically stated as follows:

dilate (f, s) = θ(c, 1)
c = f x s

where θ the threshold operation, f the mask of the input image, s the structural element.

The mask has the information required to locate corrosion-containing areas in the image. The per-element bit-wise combination of the input image and the mask is computed to visualize the corroded regions in the mask. This procedure yields the pixels of the input image whose coordinates match to pixels in the mask whose values are 1 (visually identifiable as white) while keeping the values of all other pixels at 0. (visually identified as black).

Contours are discovered and drawn on the input image to view the same areas. Contours are defined as a curve that connects all continuous points that have the same hue or intensity along the boundaries of an item in an image. Satochi Suzuki and Keiichi Abe's method is used to detect contours in the mask.

The outlines are then created on the input image to highlight the areas with corrosion. The area encompassed by contours is determined using Green's algorithm to determine the percentage of corrosion in the image.
