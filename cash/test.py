import cv2
import sys
import os
import time

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(1)

delay=6   
close_time=time.time()+delay

while True:
    # Capture frame-by-frame
    ret0, frame0 = video_capture_0.read()
    ret1, frame1 = video_capture_1.read()
    if (ret0):
        gray = cv2.cvtColor(frame0, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )
        
    if len(faces) > 0:
        many = '{} faces found!'.format(len(faces))
        #print(many)
        print('Face detected')
        print('Face match')
        print('ID match = fadhil09')
        #time.sleep(15)
        #break

    if time.time() > close_time:
         break


    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame0, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture_0.release()
cv2.destroyAllWindows()