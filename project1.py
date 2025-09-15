# Project 1

# DESC:  This project takes in a variety of images of Billards
#        Tables and spots Billard Balls along the top of the table using openCV
#        image filtering, edge detection, and shape detection


# NOTES:
#   All test images are 1080x1920p
#   Color of table is always homogenous
#   RED - White spotball with red dots
#   Green - other balls

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
    orgimg = cv.imread(sys.argv[1], 0)
    """ Unmodified Image """

    if orgimg is None:  # Debug: Check image was read
        sys.exit('ERROR: Could not read image')

    # Display unmodified image
    cv.imshow('unmodified image', orgimg)
    cv.imshow('RGB Image', orgimgRGB)

    print(orgimg)
    cv.waitKey(0)


def plotMat(Matrix):

    newMatrix = Matrix

    return newMatrix


main()
