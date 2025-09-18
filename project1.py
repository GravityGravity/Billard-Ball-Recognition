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
    orgimg = cv.imread(sys.argv[1], cv.IMREAD_COLOR_BGR)
    """ Unmodified Image """

    if orgimg is None:  # Debug: Check image was read
        sys.exit('ERROR: Could not read image')

    gaussblurimg = cv.GaussianBlur(orgimg, (3, 3), 2)

    bilaterBlurImg = cv.bilateralFilter(orgimg, 30, 150, 150)
    edges = cv.Canny(bilaterBlurImg, 35, 80)

    edges = cv.dilate(edges, (3, 3), iterations=5)
    edges = cv.erode(edges, (3, 3), iterations=3)

    Hcircle = cv.HoughCircles(
        edges, cv.HOUGH_GRADIENT_ALT, dp=1, minDist=10, param1=10, param2=0.2, minRadius=10, maxRadius=35)

    if Hcircle is not None:
        circleDet = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)

        for i in Hcircle[0, :]:
            cv.circle(circleDet, (int(i[0]), int(i[1])),
                      int(i[2]), (255, 0, 0), 3)

    # Display unmodified image
    cv.imshow('unmodified image', orgimg)
    cv.imshow('gauss filter image', gaussblurimg)
    cv.imshow('bilateral filter image', bilaterBlurImg)
    # cv.imshow('Canny edge detector', edges)
    cv.imshow('Hough Circle', circleDet)
    print(Hcircle)
    cv.waitKey(0)


main()
