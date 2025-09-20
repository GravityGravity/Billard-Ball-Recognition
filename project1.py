# Billard-Ball-Recognition

# DESC:  This project takes in a variety of images containing Billards
#        Tables and spots Billard Balls along the top of the table using openCV
#        image filtering, edge detection, and shape detection.

import sys
import numpy as np
import cv2 as cv


def main():

    # Debug: Check image path was passed
    try:
        print(f'Image path passed: {sys.argv[1]}')
    except IndexError:
        sys.exit('ERROR: No Argument for image path')

    # Read image and Check image was read
    orgimg = cv.imread(sys.argv[1], cv.IMREAD_COLOR_BGR)

    if orgimg is None:
        sys.exit('ERROR: Could not read image')

    # Cropping image to prevent circles detected outside of pool table
    height, width = orgimg.shape[:2]
    x1, y1 = 100, 100
    x2 = (orgimg.shape[1] - x1)
    y2 = (orgimg.shape[0] - y1)

    kernel = np.ones((13, 13)) / 169

    orgimg = orgimg[y1:y2, x1:x2]

    # Adding filters + color conversion for image
    grayimg = cv.cvtColor(orgimg, cv.COLOR_BGR2GRAY)
    bilaterBlurImg = cv.bilateralFilter(orgimg, 30, 150, 150)

    # Canny Edge detection with Open Operation
    edges = cv.Canny(bilaterBlurImg, 20, 60)
    edges = cv.dilate(edges, (3, 3), iterations=5)
    edges = cv.erode(edges, (3, 3), iterations=1)

    # OpenCV Circle Shape Detection Algorithm
    Hcircle = cv.HoughCircles(
        edges, cv.HOUGH_GRADIENT, dp=2, minDist=35, param1=60, param2=55, minRadius=10, maxRadius=35)

    if Hcircle is not None:
        circleDet = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        print(len(Hcircle[0, :]))  # Prints total Circles found

        # Loops: through circles and averages color within circles to print Coordinate + identify white spot-ball
        for (x, y, r) in Hcircle[0, :]:
            spot_ball = 0
            color = (255, 0, 0)

            # Color avg for identifying spot ball
            if (np.sum(grayimg[int(y) - 6: int(y) + 7, int(x) - 6: int(x) + 7] * kernel) >= 220):
                spot_ball = 1
                color = (0, 0, 255)

            # Draw Circles onto images + Print Coordinates
            cv.circle(circleDet, (int(x), int(y)), int(r), color, 2)
            cv.circle(orgimg, (int(x), int(y)), int(r), color, 2)
            print(f'{int(x) + x1} {int(y) + y1} {spot_ball}')

    # # # Display unmodified image + Canny Edges
    cv.imshow('unmodified image', orgimg)
    cv.imshow('Detected Circle + Canny Edges', circleDet)
    cv.waitKey(0)


main()
