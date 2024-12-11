import cv2

#içe aktarma
img = cv2.imread("tek.jpeg", 0)
#0 siyah veya beyaz oluştur anlamına gelir

#görselleştiriyoruz
cv2.imshow("ilk resim", img)
#klavye bağlantısı kullanıyoruz resim video açmada komut beklesin diye.
k = cv2.waitKey(0) &0xFF
if k== 27:
 cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("tek_gray.png", img)
    cv2.destroyAllWindows()
    


