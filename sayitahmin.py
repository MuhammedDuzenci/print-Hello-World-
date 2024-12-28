import random
print("Sayı Tahmin Etme Oyununa Hoşgeldiniz!")
print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

dogrusayi=random.randint(1,100)
tahminsayisi=0

while True:
    try:
        tahmin=int(input("Tahmininiz?: "))
    except ValueError:
        print("Lütfen Geçerli Bir Sayı Giriniz!")
        continue
    tahminsayisi +=1
    if tahmin < dogrusayi:
        print("Lütfen Daha Büyük Bir Sayı Giriniz!")
    elif tahmin > dogrusayi:
        print("Lütfen Daha Küçük Bir Sayı Giriniz!")
    else:
        print(f"Tebrikler! Doğru Tahmin ettin:{dogrusayi}")
        print(f"{tahminsayisi} denemede buldunuz")
        break
print("GAME OVER")