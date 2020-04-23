import numpy as np
import cv2
import os

# this two lines are for loading the videos.
# in this case the video are named as: cut1.mp4, cut2.mp4, ..., cut15.mp4
# videofiles = [n for n in os.listdir('.') if n[0]=='c' and n[-4:]=='.mp4']
# videofiles = sorted(videofiles, key=lambda item: int( item.partition('.')[0][3:]))


videofiles = [n for n in os.listdir('.') if n[0]=='c' and n[-4:]=='.mp4']
videofiles = sorted(videofiles, key=lambda item: int( item.partition('.')[0][3:]))


video_index = 0
cap = cv2.VideoCapture(videofiles[0])


fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('cutout.mp4', fourcc, 20, (640, 480))

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('cutout.avi', fourcc, 20.0, (640, 480))


while(cap.isOpened()):
    ret, frame = cap.read()
    if frame is None:
        print ("end of video " + str(video_index) + " .. next one now")
        video_index += 1
        if video_index >= len(videofiles):
            break
        cap = cv2.VideoCapture(videofiles[ video_index ])
        ret, frame = cap.read()
    cv2.imshow('frame',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
out.release()
cv2.destroyAllWindows()


print ("end.")