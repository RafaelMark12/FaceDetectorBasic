from multiprocessing.connection import wait
import cv2 as cv
#"Elsőnek megadjuk a kezdeti alap dolgokat, a képet beolvassuk, a prototípust megadjuk."

s1 = int(input("Adjon meg egy számot 1-255-ig: "))
s2 = int(input("Adjon meg egy második számot 1-255-ig: "))
s3 = int(input("Adjon meg egyharmadik számot 1-255-ig: "))
print("Ezek a számok a négyzetnek lesz RGB-ben a színek.")
vastagsag = int(input("Adja meg mekkora legyen a nagysága a négyzetnek, amivel felismeri az arcot: "))

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv.imread('arcnoi.jpg')
print("A kezdeti kép után elindul az arcfelismerése és annak a menete.")
cv.imshow('Kezdeti kep', img)
cv.waitKey(0)

print('Gyorsan vége a műveletnek')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Rajzoljunk egy négyzetet az arc köré
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (s1, s2, s3), vastagsag)
cv.imshow('Noi arc negyzettel', img)
cv.waitKey(0)

