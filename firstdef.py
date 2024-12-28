def factoriyel (numara):
    faktoriyel=1
    for i in  range (1,numara+1):
        faktoriyel*=i
    print(f"Faktoriyel:{faktoriyel}")

sayi=int(input("Lütfen Faktoriyelini Öğrenmek İstediğiniz Sayıyı Yazınız: "))
factoriyel(sayi)