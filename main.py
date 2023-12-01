import cv2
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input

model = load_model('emotion_recognition_model.h5')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)


    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]
        face = preprocess_input(face)
        emotion = model.predict(face)

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.putText(frame, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Emotion Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()