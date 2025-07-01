import tkinter as tk
from tkinter import Frame, Label, Button, Text, Checkbutton, IntVar, Entry
from PIL import Image, ImageTk
import cv2
import threading
import pyttsx3
import speech_recognition as sr
import wikipedia
from ultralytics import YOLO

# Camera and model
cap = cv2.VideoCapture(0)
yolo_model = YOLO("yolov8n.pt")

# TTS Engine
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Recognizer
recognizer = sr.Recognizer()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        try:
            audio = recognizer.listen(source, timeout=8, phrase_time_limit=10)
            return recognizer.recognize_google(audio).lower()
        except:
            return ""





def capture_and_identify():
    ret, frame = cap.read()
    if not ret:
        update_status("Failed to capture frame.")
        return

    results = yolo_model(frame)
    objects = []

    for result in results:
        for box in result.boxes:
            label = result.names[int(box.cls[0])]
            objects.append(label)

    if objects:
        obj_name = objects[0]
        update_status(f"Detected: {obj_name}")
        if speech_enabled.get():
            speak(f"I detected {obj_name}. Do you have any questions about it?")

        for _ in range(3):
            question = listen()
            if question:
                answer = google_search(f"{question} about {obj_name}")
                update_status(answer)
                if speech_enabled.get():
                    speak(answer)
                return
        update_status("No valid question detected.")
    else:
        update_status("No objects detected.")
        if speech_enabled.get():
            speak("I couldn't detect any object.")


def update_status(msg):
    status_text.config(state="normal")
    status_text.delete("1.0", tk.END)
    status_text.insert(tk.END, msg)
    status_text.config(state="disabled")


def start_detection():
    threading.Thread(target=capture_and_identify, daemon=True).start()


def speak_input_text():
    text = input_entry.get().strip()
    if text:
        update_status(f"Speaking: {text}")
        if speech_enabled.get():
            speak(text)


def update_camera():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (right_frame.winfo_width(), right_frame.winfo_height()))
        img = ImageTk.PhotoImage(Image.fromarray(frame))
        cam_label.config(image=img)
        cam_label.image = img
    root.after(10, update_camera)


def on_close():
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()


# GUI
root = tk.Tk()
root.title("Object Assistant")
root.attributes("-fullscreen", True)
root.configure(bg="#121212")
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

speech_enabled = IntVar(value=1)

main_frame = Frame(root, bg="#121212")
main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

left_frame = Frame(main_frame, bg="#1e1e2f", bd=2, relief="ridge")
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20), pady=10)

right_frame = Frame(main_frame, bg="#1e1e2f", bd=2, relief="ridge")
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, pady=10)

Label(left_frame, text="Object Detection & Voice Assistant", font=("Helvetica", 16, "bold"),
      fg="white", bg="#1e1e2f").pack(pady=(20, 10))

Button(left_frame, text="Start Detection", font=("Helvetica", 12),
       bg="#4CAF50", fg="white", relief="flat", command=start_detection).pack(ipadx=10, ipady=5, pady=(0, 10))

Checkbutton(left_frame, text="Enable Voice Output", variable=speech_enabled,
            bg="#1e1e2f", fg="white", selectcolor="#1e1e2f", font=("Helvetica", 12),
            activebackground="#1e1e2f").pack(pady=(0, 15))

Label(left_frame, text="Ask Something (optional):", font=("Helvetica", 13),
      fg="white", bg="#1e1e2f").pack()

input_entry = Entry(left_frame, font=("Helvetica", 12), bg="#2c2c3e", fg="white", insertbackground="white")
input_entry.pack(padx=20, pady=(5, 10), ipady=5, fill=tk.X)

Button(left_frame, text="Speak Output", font=("Helvetica", 12),
       bg="#3f51b5", fg="white", relief="flat", command=speak_input_text).pack(ipadx=10, ipady=5, pady=(0, 15))

Label(left_frame, text="Status / Response:", font=("Helvetica", 13),
      fg="white", bg="#1e1e2f").pack()

status_text = Text(left_frame, height=12, width=55, font=("Helvetica", 12),
                   bg="#2c2c3e", fg="white", insertbackground="white", relief="flat", wrap=tk.WORD)
status_text.pack(padx=20, pady=(5, 20))
status_text.config(state="disabled")

Button(left_frame, text="Quit", command=on_close,
       font=("Helvetica", 12), bg="#e53935", fg="white", relief="flat").pack(ipadx=10, ipady=5)

cam_label = Label(right_frame, bg="#000000")
cam_label.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

update_camera()
root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
