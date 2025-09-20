# Billard-Ball-Recognition
This project takes in a variety of images containing Billards Tables and spots Billard Balls along the top of the table using openCV image filtering, edge detection, and shape detection.

![process](https://github.com/GravityGravity/Billard-Ball-Recognition/blob/main/ImageExamples/DetectedExample.png)

## Description
Using *OpenCV* this project reads in a **1920x1080** or **1080x1920** sized image, crops the image to focus only one the main part of the billards table, then applies a bilateral filter to help with image gradient detection.
From there, Cannys Edge Detection method is ran with open operations to assist in the Hough Gradient Circle Transform Detection.  Using these two methods provides the following results on our example image.

![edges + circles](https://github.com/GravityGravity/Billard-Ball-Recognition/blob/main/ImageExamples/EdgeExample.png)

#### Ball Identification
  - Blue: Solid and Striped balls
  - Red: Spot Ball

Ball type labels are processed using kernels for color averaging at the points where circles have been spotted.  Any circles that have a mean **white** color value are labaled *spot balls* and all others are assumed to be Solid/Striped balls
### INPUT
   Expected Inputs:
   - Input Image Resolution: 1080x1920 or 1920x1080
   - Largest Area is Billard Ball Table
   - Table color is mostly the same
   - Good bright white lighting of table+
#### *Example Input:*
  > python BallMain.py ..path/Billard-Ball-Recognition/ImageExamples/02.png

![orgimgexample](https://github.com/GravityGravity/Billard-Ball-Recognition/blob/main/ImageExamples/ImageFigure.png)


### OUTPUT
This project when ran will output the following data:
- Image path passed
- Number of potential billard balls detected
- Coordinates of potential billard balls + Spot Ball Identifier {X cord, Y cord, Spot-Ball?}
- Shown Image: Detected billard balls with Edges
- Shown Image: Detected billard balls with unmodified given image
  
![output example](https://github.com/GravityGravity/Billard-Ball-Recognition/blob/main/ImageExamples/OutputExample.png)
