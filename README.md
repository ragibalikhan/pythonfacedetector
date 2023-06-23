# Face Detector Learning Project

This is a Python project that utilizes a face detection algorithm to detect and draw rectangles around faces and eyes in real-time video feed using a webcam.

## Prerequisites

Before running this project, make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- Flask
- OpenCV

## Installation

1. Clone or download the project repository to your local machine.
2. Navigate to the project directory.

   ```shell
   $ cd face_detector_learning_project
   
3. Install the required Python packages using pip.
   ```shell
   $ pip install flask opencv-python

4. Download the Haar cascade files for face and eye detection and place them in the "Haarcascades" directory in the project folder. You can find these files in the OpenCV GitHub repository:

5. - haarcascade_frontalface_default.xml
   - haarcascade_eye.xml
  
## Usage
 To run the project, follow these steps:
 1. Open a terminal or command prompt.
 2. Navigate to the project directory.
      ```shell
      $ cd face_detector_learning_project

 3. Start the Flask development server by running the following command:
     ```shell
     $ python app.py

 4. Open a web browser and go to http://localhost:5000 to access the project.

     ## Note: Make sure you have a webcam connected to your machine.

 5. The web page should display the live video feed from the webcam with rectangles around detected faces and eyes.   

    

  
   
