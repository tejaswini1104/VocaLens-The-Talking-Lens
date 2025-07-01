# 🧠 Vocalens: The Talking Lens

"Vocalens" is an AI-powered desktop application that combines real-time object detection with voice-based interaction. Built with Python, OpenCV, YOLOv8, and Tkinter, it provides visual and auditory feedback about detected objects and answers user queries using Wikipedia.

 ✨ Features:
- 🎥 Real-time webcam object detection using YOLOv8.
- 🔊 Voice output via Text-to-Speech (TTS) using `pyttsx3`.
- 🎤 Speech recognition to understand user queries.
- 🌐 Wikipedia integration to fetch answers about detected objects.
- 🖥️ Fullscreen desktop GUI built with Tkinter in a dark-themed layout.
- ✅ Option to toggle voice output on/off.
- 💬 User input for optional custom text-to-speech.

 🧰 Tech Stack:
- Python
- OpenCV
- YOLOv8 (`ultralytics`)
- pyttsx3 (TTS)
- speech_recognition
- Wikipedia API
- Tkinter (GUI)
- PIL (Image handling)


🚀 How It Works:
1. The app opens in fullscreen with webcam feed on the right.
2. Click **Start Detection** to capture and detect objects in view.
3. Detected object names are spoken (if enabled) and displayed.
4. The app listens for voice questions about the detected object.
5. Wikipedia is queried to give back answers which are shown and optionally spoken.

