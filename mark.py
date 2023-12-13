from multiprocessing.connection import wait
import cv2
#"Elsőnek megadjuk a kezdeti alap dolgokat, a képet beolvassuk, a prototípust megadjuk."

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('justdave2.jpg')
print("A kezdeti kép után elindul az arcfelismerése és annak a menete.")
cv2.imshow('Kezdeti kep  Markrol', img)
cv2.waitKey(0)

print('Gyorsan vége a műveletnek')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)


# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (125, 125, 125), 25)
cv2.imshow('Mark negyzettel', img)
cv2.waitKey(0)