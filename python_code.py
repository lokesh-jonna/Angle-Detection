import cv2
import numpy as np

def edge_detection(img, blur_ksize=3, threshold1=50, threshold2=50):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gaussian = cv2.GaussianBlur(gray, (blur_ksize, blur_ksize), 0)
    img_canny = cv2.Canny(img_gaussian, threshold1, threshold2)

    return img_canny


def draw_lines(img, lines, color=[255, 0, 0], thickness=3):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                if x2 - x1 == 0:
                    cv2.line(img, (x1, 0), (x1, img.shape[0]), color, thickness)
                else:
                    # calculate slope and y-intercept
                    m = (y2 - y1) / (x2 - x1)
                    b = y1 - m * x1

                    # calculate endpoints of line at top and bottom of image
                    y_top = 0
                    x_top = (y_top - b) / m
                    y_bottom = img.shape[0]
                    x_bottom = (y_bottom - b) / m

                    # draw line
                    cv2.line(img, (int(x_top), y_top), (int(x_bottom), y_bottom), color, thickness)


def get_angle(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

    # Remove the line that prints the detected lines

    # Rest of the code...

    # extract the angle
    angle = 0
    if lines is not None and len(lines) > 0:
        for line in lines:
            for rho, theta in line:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
                angle = np.arctan2(y2 - y1, x2 - x1)
                angle = angle * 180 / np.pi
                angle = abs(angle)
                if angle > 180:
                    angle = 360 - angle
        if angle != 0:
            return angle
    return None


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    # wait for 'q' key to start detecting object or exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

object_detected = False

while not object_detected:
    ret, frame = cap.read()

    if not ret:
        break

    angle = get_angle(frame)
    if angle is not None:
        print("Angle: {:.2f}".format(angle))
        object_detected = True

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        # save the frame as an image
        filename = "object_image.jpg"
        cv2.imwrite(filename, frame)
        print(f"Object image saved as {filename}")
        object_detected = True

cap.release()
cv2.destroyAllWindows()
