import cv2

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    _, frame = webcam.read()

    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(gray_img)

    for i in range(len(face_coordinates)):
        (x, y, w, h) = face_coordinates[i]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

    cv2.imshow('detector', frame)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break    

webcam.release()    