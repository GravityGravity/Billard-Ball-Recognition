# Project 1

# DESC:  This project takes in a variety of images of Billards
#        Tables and spots Billard Balls along the top of the table using openCV
#        image filtering, edge detection, and shape detection


# NOTES:
#   All test images are 1080x1920p
#   Color of table is always homogenous
#   RED - White spotball with red dots
#   Green - other balls

# PHASE 1:
#   50% Ball Detection rate
#   50% FAR (Incorrect detections rate)
#   50% CR (Ball classification rate)


import sys  # For command line arguments
import numpy as np
import cv2 as cv
import matplotlib as plt


def main():

    try:    # Debug: Check image path was passed
        print(f'Image path passed: {sys.argv[1]}')
    except IndexError:
        sys.exit('ERROR: No Argument for image path')

    # Read Image (0 = grayscale, 1 = BGR 'Default')
    orgimg = cv.imread(sys.argv[1], cv.IMREAD_GRAYSCALE)
    """ Unmodified Image """

    if orgimg is None:  # Debug: Check image was read
        sys.exit('ERROR: Could not read image')

    # Display unmodified image
    cv.imshow('unmodified image', orgimg)

    gaussblurimg = orgimg.copy()

    gaussblurimg = cv.GaussianBlur(gaussblurimg, (11, 11), 4)

    cv.imshow('gauss filter image', gaussblurimg)

    cv.waitKey(0)


main()
