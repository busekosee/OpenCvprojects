import cv2
import numpy as np

#resim olustur
img = np.zeros((512,512,3), np.uint8)
print(img.shape)

#3siyah resim

cv2.imshow("Siyah", img)

#çizgi
cv2.line(img, (0,0),(512,512),(0,255,0),3)

 #ilk satır resim,başlangıç nok, bitiş nok,renk,çizgi kalınlık
cv2.imshow("Cizgi",img)



#dikdörtgen
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("Dikdortgen",img)
 
#cember
#resim,merkez,yarı çap,renk
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("Cember", img)

#♦metin
cv2.putText(img,"Resim",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Metin",img)
