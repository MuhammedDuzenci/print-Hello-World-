print("Otopark Ücreti Ödeme Sistemine Hoşgeldiniz")
try:
    saat=float(input("Lütfen Otopark'ta Geçirdiniz Süreyi Yazınız: "))
    if saat <=1:
        print("Ücretiniz 50 TL")
    elif saat <=5:
        ucret=saat*30
        print("Ücretiniz",ucret,"TL")
    else:
        ucret=saat*40
        print("Ücretiniz",ucret,"TL")
except ValueError:
    print("Lütfen Sayı Cinsinden Değer Giriniz!")