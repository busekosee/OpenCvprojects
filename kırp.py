import cv2

img = cv2.imread("lenna.png")
print ("Resim boyutu:" , img.shape)
cv2.imshow("Orijinal", img)

#yeniden boyutlandıralım
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape:",imgResized.shape)
cv2.imshow("Img Resized",imgResized)

#kırp
imgCropped = img[:200,:300]
cv2.imshow("Kirpik resim",imgCropped)
