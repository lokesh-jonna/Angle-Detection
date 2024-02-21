# Angle Detection between 2 objects 

This project uses the YOLO (You Only Look Once) model to perform real-time object detection on a webcam feed. The implementation is based on the YOLOv3 model and the COCO dataset.

## Prerequisites

- Python
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- 
## Getting Started

1. Download the YOLOv3 weights, configuration file, and class names file from the official YOLO website or repository.

2. Place the downloaded files in the same directory as the Python script.

3. Run the script:

    ```bash
    python python_code.py
    ```

4. Press 'q' to exit the application.

## How it Works

- The script captures frames from the webcam and uses the YOLO model for object detection.

- Detected objects are drawn as bounding boxes with confidence scores.

- The script calculates the angle between the first two detected objects in the frame.

## Customize

- Adjust the confidence threshold (`confidence > 0.5`) in the script to control object detection sensitivity.

- Modify the code to include additional functionality or customize the output.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

## License

This project is licensed under the [MIT License](LICENSE).


Installed Modules:
1. NumPy
2. OpenCV
3. Time
4. Matplot

USES:
1. Real-time Object Detection
2. Real-time Visualization
3. Image Saving
4. Gaming
5. VR
6. Construction

