import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('car_detector.xml')
trained_body_data = cv2.CascadeClassifier('haarcascade_fullbody.xml')

webcam2 = cv2.VideoCapture('people2.mp4')

while(True):

    (read_successful, frame) = webcam2.read()

    if(read_successful):
        grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
    face_coordinates2 = trained_body_data.detectMultiScale(grayscaled_img)

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
    for (x,y,w,h) in face_coordinates2:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
    print(face_coordinates)
    print(face_coordinates2)

    cv2.imshow('clever program face detector', frame)


    key = cv2.waitKey(1)

    if(key==81 or key==113):
        break

print("Done")