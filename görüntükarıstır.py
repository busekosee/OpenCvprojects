import cv2
import matplotlib.pyplot as plt 

#karıstırma görüntüleri
img1 = cv2.imread("img1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
 #RENKLERİ DÜZELTTİK
 
plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#boyutları aynı yapmalıyız birleştirmekmiçin

#boyuta bakalım
print(img1.shape)
print(img2.shape)

#yeniden boyutlandır
img1 = cv2.resize(img1, (600,600))
print(img1.shape)

img2 = cv2.resize(img2, (600,600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırılmış resim = alpha*img1 +beta*img2
#aşağıda bu denklemin fonksiyonu var.
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)
