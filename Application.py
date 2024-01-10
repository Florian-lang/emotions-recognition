import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import read as Rd
import main as mn 

def openImage():
    filePath = filedialog.askopenfilename(title="Sélectionner une image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;")])
    if filePath:
        emotion, emotionName = Rd.emotion_on_image(filePath)
        showImage(emotion)
        emotionNameLabel.configure(text=emotionName)
        emotionNameLabel.text = emotionName

def openVideo():
    filePath = filedialog.askopenfilename(title="Sélectionner une vidéo", filetypes=[("Video files", "*.mp4;*.avi")])
    if filePath:
        showVideo(filePath)

def showImage(img):
    img.thumbnail((900, 900))
    img = ImageTk.PhotoImage(img)

    # Afficher l'image dans une fenêtre Tkinter
    imgLabel.configure(image=img)
    imgLabel.image = img

def showVideo(filePath):
    cap = cv2.VideoCapture(filePath)

    # Lire la première image
    ret, frame = cap.read()
    # Convertir l'image de BGR à RGB pour l'affichage dans Tkinter
    emotion, emotionName = Rd.emotion_on_image(filePath,frame)
    showImage(emotion)
    emotionNameLabel.configure(text=emotionName)
    emotionNameLabel.text = emotionName

    # Fonction pour lire la vidéo
    def updateVideo():
        nonlocal frame
        ret, frame = cap.read()
        if ret:
            emotion, emotionName = Rd.emotion_on_image(filePath,frame)
            showImage(emotion)
            emotionNameLabel.configure(text=emotionName)
            emotionNameLabel.text = emotionName
            emotion.thumbnail((900, 900))
            imgLabel.after(10, updateVideo)  # Mise à jour toutes les 10 ms

    # Démarrer la lecture de la vidéo
    updateVideo()

def openCamera():
    mn.openCamera()

# Créer une fenêtre Tkinter
fenetre = tk.Tk()
fenetre.geometry("300x300") 
fenetre.title("Sélection d'image et de vidéo")

# Bouton pour insérer une image
btnImage = tk.Button(fenetre, text="Insérer une image", command=openImage)
btnImage.pack(pady=10)

# Bouton pour ouvrir une vidéo
btnVideo = tk.Button(fenetre, text="Ouvrir une vidéo", command=openVideo)
btnVideo.pack(pady=10)

btnCamera= tk.Button(fenetre, text="Ouvrir la camera", command=openCamera)
btnCamera.pack(pady=10)
# Label pour afficher l'image ou la vidéo
imgLabel = tk.Label(fenetre)
imgLabel.pack()

emotionNameLabel = tk.Label(fenetre)
emotionNameLabel.pack()
# Lancer la boucle principale Tkinter
fenetre.mainloop()
