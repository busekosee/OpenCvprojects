import cv2
import time


#video ismi 
video_name = "MOT17-04-DPM.mp4"
#video içe aktar
cap = cv2.VideoCapture(video_name)

print("Genişlik:",cap.get(3))
print("Yükseklik:",cap.get(4))

#koşul koyuyorum video açıldımı boşmu
if cap.isOpened() == False:
    print("Hata")
while True:  
 ret, frame = cap.read() 

 if ret == True:
    
    time.sleep(0.01) #uyarı: kullanmazsak video çok hızlı akar
    
    cv2.imshow("Video", frame)
    #bu işlemler aslında resim için o yüzden döngüye sokuyoruzki video için olsun
 else: break
 if cv2.waitKey(1) & 0xFF == ord("q"):
     break #kendi isteiğimle çıkıyorum
cap.release() #stop capture
cv2.destroyAllWindows()  
    