import cv2
import numpy as np
 
# Webcam 'den görüntü almak için.
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Virgülden sonraki kısım derleyicinin hata vermemesi içindir.
 
# Yakalanılan görüntüyü görebilmek için while döngüsü oluşturulur.
while True:
    ret, cerceve = capture.read()
    frame = cv2.flip(cerceve, 1) # Webcami y-eksenine göre simetrisini alır. Düzgün olması açısından bu işlem yapılır. 0 veya -1 yazılırsa x-eksenine ve orjine göre yanıması alınır.


# Renk tespiti için maskeleme kullanılır. Mask frame 'ler üzerine uygulanır ve bir renk aralığı belirlenir. Frame içinde kalan renkler korunur ve diğer renkler atılır. BGR yerine HSV renk uzayı kullanacağım çünkü bu uzayda aynı rengin bir çok tonunu rahatça algılayabiliriz.

    hsv_cerceve = cv2.cvtColor(cerceve, cv2.COLOR_BGR2HSV) # Öncelikle frame 'ler HSV formatına çevirilmeli.

# Bu değerler arasındaki renkleri korusun diğer renkleri atsın. "https://alloyui.com/examples/color-picker/hsv.html"
    
    altdeger_kirmizi = np.array([0, 100, 100])      #169, 100, 100      0, 100, 100   Bu değerler
    ustdeger_kirmizi = np.array([10, 255, 255])     #189, 255, 255     10, 255, 255   daha hassas deneyebilirsin.

# Bu fonksiyon alt ve üst değerde kalan renkleri görüntüde tutacak ve diğer tüm renkleri silecektir.
    kirmizi_maske = cv2.inRange(hsv_cerceve, altdeger_kirmizi, ustdeger_kirmizi)
    kirmizi = cv2.bitwise_and(cerceve, cerceve, mask = kirmizi_maske) # Bu sayede maskeleme ekranında yeşil rengi beyaz olarak değil yeşil olarak görmüş olacağız.


    cv2.imshow("Kamera", cerceve) # Kamera görüntüsü.
    cv2.imshow("Kirmizi Maske Beyaz", kirmizi_maske) # Beyaz renkli filtre ekranı.
    cv2.imshow("Sadece Kirmizi Renk Ekrani", kirmizi) # Kırmızı renkli filtre ekranı.

    if cv2.waitKey(1) & 0xFF == ord('q'): # Kodu durdurmak için "q" tuşuna basılmalıdır aksi takdirde kod sürekli çalışmaya devam edecetir.
        break
 
capture.release()
cv2.destroyAllWindows()
