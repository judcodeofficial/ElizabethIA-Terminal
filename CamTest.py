import cv2
import numpy as np

#face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt_tree.xml')
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')
#face_cascade = cv2.CascadeClassifier('haarcascades/cars.xml')
captura = cv2.VideoCapture('rtsp://username:password@192.168.68.115:554/cam/realmonitor?channel=1&subtype=0')
#captura = cv2.VideoCapture(0)

# define some text properties
font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 60)
fontScale = 1
fontColor = (255, 0, 0)
lineType = 2

while True:
    ret, frame = captura.read()
    frame = cv2.resize(frame, (960, 540), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.35, 4)

    cv2.putText(
            frame,
            'Elizabeth Eyes V1',
            bottomLeftCornerOfText,
            font,
            fontScale,
            fontColor,
            lineType)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Facial recognition in real time - Elizabeth v1', frame)
    k = cv2.waitKey(10)&0xFF
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows()