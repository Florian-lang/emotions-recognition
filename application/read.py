import cv2
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from PIL import Image


# Charger le modèle d'émotion
model = load_model('data/emotion_recognition_model.h5')

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

    if detect_visage(frame) is False:
        emotion_name = "Aucun visage détecté"

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    return Image.fromarray(frame_rgb), emotion_name


def detect_visage(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)

    for (x, y, w, h) in faces:
        capturedFace = frame[y:y + h, x:x + w]

        resizedFace = cv2.resize(capturedFace, (96, 96))
        reshapeFace = preprocess_input(resizedFace).reshape(96, 96, 3)
        expendedFaceDimenssion = np.expand_dims(reshapeFace, axis=0)

        emotion = model.predict(expendedFaceDimenssion)

        emotionName = emotion_labels[np.argmax(emotion)]

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

        cv2.putText(frame, emotionName, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return True
