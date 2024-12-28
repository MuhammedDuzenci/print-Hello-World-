""""""""""""""""
for i in range (1,10):
    print(i * "-")
"""""""""""""""""
print ("Faktöriyel Hesaplama Sistemine Hoşgeldiniz !")

while True:
    faktoriyel=1
    sayi=int(input("Faktöriyelini Bulmak İstediğiniz Sayıyı Giriniz: "))
    if sayi <=0:
        print("Lütfen 0'dan Büyük Bir Sayı Giriniz !")
    else:
        for i in range(1,sayi+1):
            faktoriyel *= i
        print("Faktoriyel: ",faktoriyel)
        break