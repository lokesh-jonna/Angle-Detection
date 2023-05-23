# Angle-Detection
This project is done in Hackathon under 24hrs in RGMCET

In this repository, we are gonna calculate angle between two flat objects
The main objective of the code is to detect objects in a live video stream and calculate the angle of the detected object.
1. The necessary libraries, cv2 (OpenCV) and numpy, are imported.

2. The edge_detection function takes an image as input and performs edge detection using the Canny edge detection algorithm. It converts the image to grayscale, applies Gaussian blur, and then detects edges using Canny edge detection. The resulting edge image is returned.

3. The draw_lines function is responsible for drawing lines on the image. It takes the image, a set of lines, color, and thickness as inputs. It iterates through the lines and draws each line on the image using the cv2.line function. Additionally, it handles cases where the line is vertical, drawing a vertical line from top to bottom of the image.

4. The get_angle function calculates the angle of the detected object in the image. It converts the image to grayscale, applies Canny edge detection, and uses the Hough transform to detect lines in the edge image. The detected lines are then iterated, and for each line, the function calculates the angle using trigonometry. The angle is returned.

5. The code initializes the video capture using cv2.VideoCapture(0), which captures video from the default camera.

6. A while loop is used to continuously read frames from the video capture. Inside the loop, the frame is displayed using cv2.imshow. The loop breaks if the user presses the 'q' key.

7. Another while loop is used to detect an object and calculate its angle. This loop continues until an object is detected or the user presses the 'q' key. Inside the loop, a frame is read from the video capture, and the get_angle function is called to calculate the angle. If an angle is obtained, it is printed, and the loop is terminated. The frame is displayed, and the loop breaks if the user presses the 'q' key or 's' key to save the frame as an image.

8. After the loops end, the video capture is released, and all windows are closed using cap.release() and cv2.destroyAllWindows().

Installed Modules :
1. NumPy
2. OpenCV
3. Time
4. Matplot

USES :
1. Real-time Object Detection
2. Flexibility
3. Real-time Visualization
4. Image Saving
5. Platform Independence
6. Gaming
7. VR
8. Construction

TEAM MEMBERS

Lokesh J(Lead)
Nanda Kishore R
Tejaswini M
Hussain S
Subhash
Priyanka R
Muni Kishore P
