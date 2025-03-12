import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
import cv2
from PIL import Image, ImageTk
import pyautogui

vid = cv2.VideoCapture(0) 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

root = tk.Tk()
root.geometry('370x400')
root.title("Cursor-Flow")
root.configure(bg='white')  
root.resizable(False, False)

def open_camera(): 
    _, frame = vid.read()
    frame = cv2.resize(frame, (180, 150))
    
    height, width, channels = frame.shape

    # Calculate center of the frame
    center_x = width // 2 
    center_y = (height // 2) + 10
    box_x_min = center_x - 20
    box_y_min = center_y - 20
    box_x_max = center_x + 20
    box_y_max = center_y + 20
    cv2.rectangle(frame, (box_x_min, box_y_min), (box_x_max, box_y_max), (0, 0, 255), 2)
    face = face_cascade.detectMultiScale(frame, scaleFactor=1.1 , minNeighbors=5)
    for (x, y, w, h) in face:
        face_center_x = x + w // 2
        face_center_y = y + h // 2
        cv2.circle(frame, (face_center_x, face_center_y), 5, (0, 255, 0), 2)
        if face_center_x < box_x_min:
            pyautogui.moveRel(-10, 0, duration = 0.01)
        elif face_center_x > box_x_max:
            pyautogui.moveRel(10, 0, duration = 0.01)

        if face_center_y < box_y_min:
            pyautogui.moveRel(0, -10, duration = 0.01)
        elif face_center_y > box_y_max:
            pyautogui.moveRel(0, 10, duration = 0.01)

    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    captured_image = Image.fromarray(opencv_image) 
    photo_image = ImageTk.PhotoImage(image=captured_image) 

    # Displaying photoimage in the label 
    video_label.photo_image = photo_image 
    video_label.configure(image=photo_image) 
    video_label.after(10, open_camera) 

image = PhotoImage(file="header.png")

image_label = tk.Label(root, image=image)
image_label.pack() 

# Camera Frame
cam_frame = tk.Frame(root, bg="lightblue", width=300, height=50)
cam_frame.pack(padx=20, pady=20)  
video_label = Label(cam_frame)
video_label.pack()

# Button Frame
btn_frame = tk.Frame(root, bg="lightblue", width=300, height=50)
btn_frame.pack(padx=20, pady=20) 

# Common styling options
button_style = {
    'activebackground': 'lightgreen',
    'bg': 'lightgray',
    'cursor': 'hand2',
    'fg': 'black',
    'font': ('Arial', 10),
    'width': 10
}

# Start Button
start_btn = tk.Button(btn_frame, text="Start", command=open_camera, **button_style)
start_btn.pack(side="left", padx=10)

# Stop Button
stop_btn = tk.Button(btn_frame, text="Stop", command=root.destroy, **button_style)
stop_btn.pack(side="left", padx=10)

root.mainloop()
