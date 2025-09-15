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

    blurimg = orgimg.copy()
    kernel = np.ones((5,5), np.int64) / 25
    print(kernel)
    blurimg = cv.filter2D(blurimg, -1, kernel)

    cv.imshow('filter image', blurimg)


    cv.waitKey(0)


def histogram(Mat):
    """
    Prints historgram
    """

    hist_r = cv2.calcHist('img')
    hist_b = cv2.calcHist()
    hist_g = cv2.calcHist()

    plt.plot(hist_r, color='r')
    plt.plot(hist_b, color='b')
    plt.plot(hist_g, color='g')

    return


def plotMat(Mat):
    """
    Prints color plot
    """

    newMatrix = Matrix

    return newMatrix

# To represent colors in a


main()
