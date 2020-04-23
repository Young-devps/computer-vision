import urllib.request
import cv2
import numpy as np

url='http://192.168.43.1:8080/shot.jpg'

while True:
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)

    
    img=cv2.imdecode(imgNp,-1)
    print(img)

    # all the opencv processing is done here
    imgRes = cv2.resize(img, (720, 480))
    cv2.imshow('test',imgRes)
    if ord('q')==cv2.waitKey(10):
        exit(0)