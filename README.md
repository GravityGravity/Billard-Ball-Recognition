# Billard-Ball-Recognition
This project takes in a variety of images containing Billards Tables and spots Billard Balls along the top of the table using openCV image filtering, edge detection, and shape detection.

![process](https://github.com/GravityGravity/Billard-Ball-Recognition/blob/main/ImageExamples/DetectedExample.png)

## Description
Using OpenCV this project reads in a 1920x1080 or 1080x1920 sized image, crops the image to focus only one the main part of the billards table, then applies a bilateral filter to help with image gradient detection.
From there, Cannys Edge Detection method is ran with open operations to assist in the Hough Gradient Transform Detection.  Using these two methods provides the following results on our example image.

![edges + circles](https://github.com/GravityGravity/Billard-Ball-Recognition/blob/main/ImageExamples/EdgeExample.png)

#### Identifiers
  Blue -> Solid and Striped balls
  
  Red -> Spot Ball
