print("Yaş Hesaplama Sistemine Hoşgeldiniz")
try:
    dogum=int(input("Lütfen Doğum Tarihinizi Giriniz: "))
    yas=2025-dogum
    if yas <=4:
        print("Bebeksin",yas)
    elif yas <=10:
        print("Çocuksun",yas)
    elif yas <=18:
        print("Genç",yas)
    elif yas <=40:
        print("Daha Genç",yas)
    elif yas <=60:
        print("Yaşlı")
    elif yas <=80:
        print("İhtiyar Delikanlı",yas)
    else:
        print("Yürüyen Ölü",yas)
except ValueError:
    print("Lütfen Sayı Değerinden Doğum Tarihinizi Giriniz!")