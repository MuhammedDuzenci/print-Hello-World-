print  ("Öğrenci Kayıt Etme Uygulamasına Hoşgeldiniz.")
isim=(input("Öğrenci'nin Adını Yazınız: "))
soyisim=(input("Öğrenci'nin Soyadını Yazınız: "))
sinif=(input("Öğrenci'nin Sınıfını Yazınız: "))

bilgiler= [isim,soyisim,sinif]

print ("Bilgiler Kayıt Sistemine Kayıt Ediliyor.....")

print ("Öğrenci'nin Adı: {}\n Öğrenci'nin Soyadı: {}\n Öğrenci'nin Sınıfı:{}".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print ("Öğrenci Başarıyla Sisteme Kayıt Edildi.")