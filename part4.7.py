import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haar/haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

def funcname(self, parameter_list):
    """[summary]
    
    Arguments:
        parameter_list {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return parameter_list


while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()