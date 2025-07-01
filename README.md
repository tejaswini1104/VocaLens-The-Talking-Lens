# 🧠 Vocalens: The Talking Lens

Vocalens is an AI-powered assistant that combines real-time object detection with voice-based interaction. Built with Python, OpenCV, YOLOv8, and Tkinter, it provides visual and voice-based feedback about detected objects and answers user questions by performing an internet search.

✨ Features:
- 🎥 Real-time webcam object detection using YOLOv8.
- 🔊 Voice output using Text-to-Speech (`pyttsx3`).
- 🎤 Voice recognition to understand user questions.
- 🌐 Online search to answer questions about detected objects.
- 🖥️ Fullscreen Tkinter-based graphical interface with dark theme.
- ✅ Toggleable voice output.
- 💬 User text input for speaking custom messages.

🧰 Tech Stack:
- Python
- OpenCV
- YOLOv8 (`ultralytics`)
- pyttsx3 (TTS)
- speech_recognition
- Internet Search (custom function)
- Tkinter
- PIL (Image handling)

🚀 How It Works:
1. The GUI launches in fullscreen mode with live webcam feed.
2. Press **Start Detection** to identify objects in the camera view.
3. The app announces the detected object (if voice is enabled).
4. It listens for a follow-up question about the object.
5. Using an internet search, it fetches and reads a relevant answer.

