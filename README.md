# Cursor-Flow (Basic Camera Display)

This is a basic Python application using Tkinter, OpenCV, and PyAutoGUI to display a live webcam feed within a simple GUI. It serves as a foundational step towards a more advanced head-controlled cursor application.

## Prerequisites

* Python 3.x
* OpenCV (`opencv-python`)
* Pillow (PIL)
* PyAutoGUI (`pyautogui`)

## Installation

1.  **Install Python Libraries:**

    ```bash
    pip install opencv-python Pillow pyautogui
    ```

2.  **Run the Application:**

    Save the Python code as `app.py` and execute it:

    ```bash
    python app.py
    ```

## Usage

1.  **Start:** Click the "Start" button to begin displaying the webcam feed.
2.  **Stop:** Click the "Stop" button to close the application and release the webcam.

## Functionality

* Displays a live webcam feed within a Tkinter window.
* Includes "Start" and "Stop" buttons for controlling the camera display.
* Draws a red rectangle in the center of the camera feed.
* Includes pyautogui, for future cursor control.

## Code Explanation

* **Tkinter:** Used for creating the graphical user interface.
* **OpenCV:** Used for capturing and processing the webcam feed.
* **Pillow (PIL):** Used for converting OpenCV images to Tkinter PhotoImage objects.
* **PyAutoGUI:** Used for cross-platform GUI automation. This is included for future cursor control implementation.
* The code captures frames from the webcam, resizes them, draws a rectangle in the center, converts them to a format suitable for Tkinter, and displays them in a label.
* The `open_camera()` function is called repeatedly using `video_label.after()` to create a continuous video stream.
* The `stop_camera()` function releases the webcam and closes the application.

## Planned Improvements (Future Development)

* Implement head tracking using OpenCV or MediaPipe.
* Map head movements to mouse cursor movements using PyAutoGUI.
* Add clicking functionality (dwell clicking, voice commands, etc.).
* Enhance the user interface with more settings and customization options.
* Add calibration features.

## Notes

* Ensure your webcam is properly connected and accessible.
* This is a very basic application, and is meant to be the first step in creating a more complete cursor control application.
* Pyautogui is added, in preperation for mouse control.
