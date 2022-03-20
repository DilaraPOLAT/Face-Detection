import  cv2

img=cv2.imread("C:\\udemyopencv\\haar_cascade\\test_images\\face.png")

face_cascade=cv2.CascadeClassifier("C:\\udemyopencv\\haar_cascade\\haar_cascade_file\\frontalface.xml") #cascade dosyamı ekledim
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #resmi gri formata ceviridik

faces=face_cascade.detectMultiScale(gray,1.3,7)#bu cascade dosyasını kullanıp resimdeki yuzun koordinatlarını bul
#img,olceklendirme degeri=kac oranda resmi kucultecegim ,belli bir bolgede en az 4 pencere bulsun ben onun yuz oldugunu anlayayım
#faces bir tuple icerisinde-> 4 adet degsiken var 2'si yuzun sol ust koordinatını diger 'si yukseklik ve genişlik
#NOT=face_cascade.detectMultiScale(gray,1.3,4) yazdıgımızda 2 yuz buldu daha iyi bir sonuc icin pencere sayısını artırdım

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)#img,sol alt koordinatları, sag alt koordinatarı,renk,kalınlık

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()