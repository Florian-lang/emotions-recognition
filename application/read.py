import cv2
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from PIL import Image


# Charger le modèle d'émotion
model = load_model('emotion_recognition_model.h5')

# Étiquettes d'émotion
emotion_labels = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']


def emotion_on_image(image_path, frame=None):
    if frame is None:
        frame = cv2.imread(image_path)

    # Traiter l'image (resize, prétraitement, etc. selon les besoins)
    resized_face = cv2.resize(frame, (96, 96))  # Ajuster la taille selon les besoins
    processed_face = preprocess_input(resized_face).reshape(96, 96, 3)
    expanded_face_dimension = np.expand_dims(processed_face, axis=0)

    # Prédire l'émotion
    emotion_prediction = model.predict(expanded_face_dimension)
    emotion_name = emotion_labels[np.argmax(emotion_prediction)]
    detect_visage(frame)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    return Image.fromarray(frame_rgb), emotion_name


def detect_visage(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
