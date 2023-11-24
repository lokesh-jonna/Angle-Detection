import cv2
import numpy as np

# Load YOLO model
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Open camera capture
cap = cv2.VideoCapture(0)

# Initialize variables to store detected objects
detected_objects = []

while True:
    # Read frame from the camera
    ret, frame = cap.read()

    # Preprocess input
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)

    # Perform object detection
    output_layers_names = net.getUnconnectedOutLayersNames()
    outputs = net.forward(output_layers_names)

    # Postprocess the results
    boxes = []
    confidences = []
    class_ids = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5:  # Adjust confidence threshold as needed
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                w = int(detection[2] * frame.shape[1])
                h = int(detection[3] * frame.shape[0])
                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # Apply non-maximum suppression to remove redundant boxes
    indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    # Draw bounding boxes and labels
    font = cv2.FONT_HERSHEY_SIMPLEX
    colors = np.random.uniform(0, 255, size=(len(classes), 3))

    if len(indices) > 0:
        detected_objects = []  # Clear the list of detected objects for the current frame
        for i in indices.flatten():
            x, y, w, h = boxes[i]
            label = classes[class_ids[i]]
            confidence = confidences[i]
            color = colors[class_ids[i]]

            cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 5), font, 0.5, color, 2)

            detected_objects.append((x, y, x + w, y + h, label))

    # Calculate angle between newly added objects when there are at least two
    if len(detected_objects) >= 2:
        object1, object2 = detected_objects[:2]
        x1, y1, x2, y2, label1 = object1
        x3, y3, x4, y4, label2 = object2

        # Calculate the angle between the two objects
        angle_between_objects = np.degrees(np.arctan2(y4 - y3, x4 - x3) - np.arctan2(y2 - y1, x2 - x1))

        # Display the calculated angle on the frame
        cv2.putText(frame, f"Angle: {angle_between_objects:.2f}", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

        print("Angle between objects: {:.2f}".format(angle_between_objects))

    # Display the frame
    cv2.imshow("Object Detection", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
