vize=int(input("Vize Notunu Giriniz: "))
final=int(input("Final Notunu Giriniz:  "))
ortalama=(vize*4/10)+(final*6/10)
if ortalama >=60:
    print("Dönemi Başarıyla Geçtiniz Tebrikler !",ortalama)
else:
    print("Maleesef Dönemiden Geçemediniz !",ortalama)