from multiprocessing.connection import wait
import cv2 as cv
#"Elsőnek megadjuk a kezdeti alap dolgokat, a képet beolvassuk, a prototípust megadjuk."

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv.imread('justdave2.jpg')
print("A kezdeti kép után elindul az arcfelismerése és annak a menete.")
cv.imshow('Kezdeti kep  Markrol', img)
cv.waitKey(0)

print('Gyorsan vége a műveletnek')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)


# Draw rectangle around the faces
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (125, 125, 125), 25)
cv.imshow('Mark negyzettel', img)
cv.waitKey(0)