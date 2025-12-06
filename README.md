# AI Virtual Mouse using Computer Vision

This project implements a touchless mouse controller using Python, OpenCV, and MediaPipe. It tracks hand landmarks in real-time to control the cursor and perform click actions based on finger gestures.

## 🛠️ Technologies Used
* Python 3.11
* **OpenCV:** For video capture and image processing.
* **MediaPipe:** For high-speed hand tracking and landmark extraction.
* **PyAutoGUI:** For controlling the operating system mouse cursor.

## 🚀 How It Works
1.  **Hand Tracking:** The system detects 21 hand landmarks using MediaPipe.
2.  **Cursor Movement:** The Index Finger tip coordinates are mapped to the screen resolution.
3.  **Clicking Mechanism:** A "Click" is triggered when the Euclidean distance between the Thumb and Index finger drops below a threshold (visualized by a green indicator).

## 💻 How to Run
```bash
pip install opencv-python mediapipe pyautogui
python virtual_mouse.py
