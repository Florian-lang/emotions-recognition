import cv2
import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input

model = load_model('emotion_recognition_model.h5')

emotionLabels = ['Anger', 'Contempt', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']


def open_camera():
    cap = cv2.VideoCapture(0)

    while True:
        _, frame = cap.read()

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)

        for (x, y, w, h) in faces:
            captured_face = frame[y: y + h, x: x + w]

            resized_face = cv2.resize(captured_face, (96, 96))
            reshape_face = preprocess_input(resized_face).reshape(96, 96, 3)
            expended_face_dimenssion = np.expand_dims(reshape_face, axis=0)

            emotion = model.predict(expended_face_dimenssion)

            emotion_name = emotionLabels[np.argmax(emotion)]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2.putText(frame, emotion_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        cv2.imshow('Emotion Recognition', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
