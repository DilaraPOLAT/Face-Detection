# 1.Kullanacagımız kutuphaneyi calısmamıza dahil edelim
import cv2

#2.webcamden veya harici bir kameradan goruntu almak ıcın 0,1 gibi degerler yazarız.Webcam icin bu deger 0'dır.
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#3.Kullanacagımız cascade dosyasını calısmamıza dahil edelim
face_cascade = cv2.CascadeClassifier(
    "C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\frontalface.xml")  # cascade dosyamı ekledim
#4.sonsuz bir dongu ile her kareyi(frame) tek tek inceleyelim
while True:
    #5.her kareyi tek tek okuyalım
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    #6.haar like ozellikleri kolay algılayabilmek ıcın her bir kareyi boz(gri)tonlara cvirelim.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret == False:
        break

    faces = face_cascade.detectMultiScale(gray, 1.3,7)  # bu cascade dosyasını kullanıp resimdeki yuzun koordinatlarını bul
    # img,olceklendirme degeri=kac oranda resmi kucultecegim ,belli bir bolgede en az 4 pencere bulsun ben onun yuz oldugunu anlayayım
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0XFF == ord("q"):
        break

cap.release()  # videoyu serbest bırakıyorum eger bunu yapmazsam ne olur? videoyu kullanamam hata verir video baska bir islem icin calısıyor.
cv2.destroyAllWindows()

