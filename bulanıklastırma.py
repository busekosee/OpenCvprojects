import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

#blurring detayı azaltır gürültüyü engeller
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

#ortalama bulanıklaştırma kutu piksellerin ortalamasını alıyoruz.
#merkeze yazıyoruz 

dst2 = cv2.blur(img, ksize =(3,3))
plt.figure(),plt.imshow(dst2),plt.axis("off"),plt.title("ortalama blur")

#♥gaussian blur
gb = cv2.GaussianBlur(img, ksize=(3,3), sigmaX =7)
plt.figure(),plt.imshow(gb),plt.axis("off"),plt.title("Gauss Blur")

#•medyan blur piksellerin medyanı alınır
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb),plt.axis("off"),plt.title("Medyan Blur")


#noise oluşturuyoruz
def gaussianNoise(image):
    row,col,ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy =image +gauss
    return noisy
#gürültüyü eklemek için normalize etmemiz lazım 0 ve 1 arasına .
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage),plt.axis("off"),plt.title("Gauss Noisy"),plt.show()

#gürültüyü blur ile azaltırız
gb2 = cv2.GaussianBlur(img, ksize=(3,3), sigmaX =7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title(" with Gauss Blur")

#tuz karabiber gürültüsü siyah beyaz noktalar
def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    
    # Tuz (beyaz) gürültü
    num_salt = int(np.ceil(amount * image.size * s_vs_p))
    coords = [np.random.randint(0, i-1, num_salt) for i in image.shape]
    noisy[coords[0], coords[1], coords[2]] = 255
    
    # Biber (siyah) gürültü
    num_pepper = int(np.ceil(amount * image.size * (1 - s_vs_p)))
    coords = [np.random.randint(0, i-1, num_pepper) for i in image.shape]
    noisy[coords[0], coords[1], coords[2]] = 0
    
    return noisy


spImage = saltPepperNoise(img)
plt.figure(),plt.imshow(spImage),plt.axis("off"),plt.title(" SP Image")

mb2 = cv2.medianBlur(spImage, ksize=3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("Medyan Blur Uygulanmış")
plt.show()
