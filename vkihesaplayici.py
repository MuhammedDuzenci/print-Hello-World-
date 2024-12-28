print("Vücut Kilo İndeksi Hesaplama Makinesine Hoşgeldiniz!")
try:
    boy=float(input("Lütfen Metre Cinsinden Boyunuzu Giriniz: "))
    kilo=float(input("Lütfen Kilogram Cinsinden Kilonuzu Giriniz: "))
    vki=kilo/(boy*boy)
    if vki <=18:
        print("Çok Zayıfsın Doktora Git",vki)
    elif vki <=25:
        print("Normal kilodasınız",vki)
    elif vki <=30:
        print("Kilolusun",vki)
    elif vki <=40:
        print("Obezsin",vki)
    else:
        print("Aşırı Kilolusun Doktora Git",vki)
except ValueError:
    print("Lütfen Sayı Cinsinden Giriniz!")
