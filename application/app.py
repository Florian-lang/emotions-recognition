import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import cv2
import read as Rd
import camera as camera


def open_image():
    selected_file_path = filedialog.askopenfilename(
        title="Sélectionner une image",
        filetypes=[
            ("Image files", "*.png"),
            ("Image files", "*.jpg"),
            ("Image files", "*.jpeg")
        ]
    )

    if selected_file_path:
        emotion, emotion_name = Rd.emotion_on_image(selected_file_path)
        show_image(emotion)
        emotionNameLabel.configure(text=emotion_name)
        emotionNameLabel.text = emotion_name 


def open_video():
    selected_file_path = filedialog.askopenfilename(title="Sélectionner une vidéo", filetypes=[("Video files", "*.mp4"),("Video files", "*.mov")])
    if selected_file_path:
        show_video(selected_file_path)


def show_image(img):
    img.thumbnail((900, 900))
    img = ImageTk.PhotoImage(img)

    imgLabel.configure(image=img)
    imgLabel.image = img


def show_video(file_path):
    cap = cv2.VideoCapture(file_path)

    _, frame = cap.read()

    emotion, emotion_name = Rd.emotion_on_image(file_path, frame)
    show_image(emotion)
    emotionNameLabel.configure(text=emotion_name)
    emotionNameLabel.text = emotion_name

    def update_video():
        nonlocal frame
        ret, frame = cap.read()
        if ret:
            emotion, emotion_name = Rd.emotion_on_image(file_path, frame)
            show_image(emotion)
            emotionNameLabel.configure(text=emotion_name)
            emotionNameLabel.text = emotion_name
            emotion.thumbnail((900, 900))
            imgLabel.after(10, update_video)

    update_video()


def open_camera():
    camera.open_camera()


fenetre = tk.Tk()
fenetre.geometry("300x300")
fenetre.title("Sélection d'image et de vidéo")

btnImage = tk.Button(fenetre, text="Insérer une image", command=open_image)
btnImage.pack(pady=10)

btnVideo = tk.Button(fenetre, text="Ouvrir une vidéo", command=open_video)
btnVideo.pack(pady=10)

btnCamera = tk.Button(fenetre, text="Ouvrir la camera", command=open_camera)
btnCamera.pack(pady=10)

imgLabel = tk.Label(fenetre)
imgLabel.pack()

emotionNameLabel = tk.Label(fenetre)
emotionNameLabel.pack()

fenetre.mainloop()
