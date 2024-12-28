print("Hesap Makinesine Hoşgeldiniz !")
while True:
    sayi1=int(input("Sayı giriniz: "))
    sayi2=int(input("Bir sayı daha giriniz: "))
    print("1.Toplama")
    print("2.Çıkartma")
    print("3.Çarpma")
    print("4.Bölme")
    islem=int(input("Lütfen Yapacagınız İşlemi Tuşlayın: "))

    if islem ==1:
        sonuc=sayi1+sayi2
        print("İşleminizin Sonucu:",sonuc)
        break
    elif islem ==2:
        sonuc=sayi1-sayi2
        print("İşleminizin Sonucu:",sonuc)
        break
    elif islem ==3:
        sonuc=sayi1*sayi2
        print("İşleminizin Sonucu:",sonuc)
        break
    elif islem ==4:
        sonuc=sayi1/sayi1
        print("İşleminizin Sonucu:",sonuc)
        break
    else:
        print("Lütfen Geçerli Sayı Tuşlayınız !")