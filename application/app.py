import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import cv2
import read as Rd
import camera as camera


def open_image():
    selected_file_path = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;")])
    if selected_file_path:
        emotion, emotion_name = Rd.emotion_on_image(selected_file_path)
        show_image(emotion)
        emotionNameLabel.configure(text=emotion_name)
        emotionNameLabel.text = emotion_name


def open_video():
    selected_file_path = filedialog.askopenfilename(title="Sélectionner une vidéo", filetypes=[("Video files", "*.mp4;*.avi")])
    if selected_file_path:
        show_video(selected_file_path)


def show_image(img):
    img.thumbnail((300, 300))
    img = ImageTk.PhotoImage(img)

    # Afficher l'image dans une fenêtre Tkinter
    imgLabel.configure(image=img)
    imgLabel.image = img


def show_video(file_path):
    cap = cv2.VideoCapture(file_path)  # Define the variable "cap" to capture video from the default camera

    _, frame = cap.read()

    # Convertir l'image de BGR à RGB pour l'affichage dans Tkinter
    emotion, emotion_name = Rd.emotion_on_image(file_path, frame)
    show_image(emotion)
    emotionNameLabel.configure(text=emotion_name)
    emotionNameLabel.text = emotion_name

    # Fonction pour lire la vidéo
    def update_video():
        nonlocal frame
        ret, frame = cap.read()
        if ret:
            emotion, emotion_name = Rd.emotion_on_image(file_path, frame)
            show_image(emotion)
            emotionNameLabel.configure(text=emotion_name)
            emotionNameLabel.text = emotion_name
            emotion.thumbnail((900, 900))
            imgLabel.after(10, update_video)  # Mise à jour toutes les 10 ms

    # Démarrer la lecture de la vidéo
    update_video()


def open_camera():
    camera.openCamera()


# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.geometry("500x400")
fenetre.title("Sélection d'image et de vidéo")
frame_boutons = tk.Frame(fenetre)
frame_boutons.pack(side=tk.LEFT, padx=10)

# Bouton pour insérer une image
btnImage = tk.Button(frame_boutons, text="Insérer une image", command=open_image)
btnImage.pack(pady=10)

# Bouton pour ouvrir une vidéo
btnVideo = tk.Button(frame_boutons, text="Ouvrir une vidéo", command=open_video)
btnVideo.pack(pady=10)

btnCamera = tk.Button(frame_boutons, text="Ouvrir la camera", command=open_camera)
btnCamera.pack(pady=10)

# Label pour afficher l'image ou la vidéo
# Frame pour l'image à droite
frame_image = tk.Frame(fenetre,borderwidth=2,relief="solid")
frame_image.pack(side=tk.RIGHT, padx=10)

imgLabel = tk.Label(frame_image,borderwidth=2,relief="solid",width=200,height=200)
imgLabel.pack()

emotionNameLabel = tk.Label(frame_image)
emotionNameLabel.pack()

# Lancer la boucle principale Tkinter
fenetre.mainloop()
