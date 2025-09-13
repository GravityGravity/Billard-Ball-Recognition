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

# Debug
try:
    print(f'Image path passed: {sys.argv[1]}')
except IndexError:
    print('ERROR: No Argument for image path')
