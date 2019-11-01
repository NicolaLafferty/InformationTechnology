import cv2
from datetime import datetime

cam = cv2.VideoCapture(0) # select camera feed
cam.set(cv2.CAP_PROP_FPS, 60) # set frame rate
cam.set(3, 1280) # set x resolution 1920
cam.set(4, 720) # set y resolution 720p 1080

font = cv2.FONT_HERSHEY_TRIPLEX

fourcc = cv2.VideoWriter_fourcc(*'XVID')    # set codec  (*'DIVX)

                    # file name    codec  FPS  output resolution
out = cv2.VideoWriter('output.avi', fourcc, 20, (1280, 720))

while True:
    re, img = cam.read() # setting the camera feed to return an image

    img = cv2.flip(img, 1) # flip to mirror view - x axis
    #           video             string        position  font size colour  stroke
    cv2.putText(img, "You are being recorded", (300, 400), font, 2, (255,0,0), 2, cv2.LINE_AA)
    cv2.putText(img, str(datetime.now()), (900, 600), font, .5, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("Nicola's Video", img) # displays camera feed window

    out.write(img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # wait for esc key to end loop
        break

cam.release()
cv2.destroyAllWindows()