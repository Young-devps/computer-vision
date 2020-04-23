import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# video_writer = cv2.VideoWriter('outeringe.avi', fourcc, 20.0, (640, 480))


# fourcc = cv2.VideoWriter_fourcc(*'vp90')
# video_writer = cv2.VideoWriter('outeringe.webm', fourcc, 20, (640, 480))


# fourcc = cv2.VideoWriter_fourcc(*'MP4V')
fourcc = cv2.VideoWriter_fourcc(*'X264')
video_writer = cv2.VideoWriter('montage.mp4', fourcc, 20, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video_writer.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()