print("Sosyal Medya Platformuna Hoşgeldiniz!")

defkullaniciadi=("muhammed")
defsifre=("1234")

kullaniciadi=(input("Lütfen Kullacını Adınızı Giriniz: "))
kullanicisifresi=(input("Lütfen Şifrenizi Giriniz: "))

if ((kullaniciadi == defkullaniciadi) and (kullanicisifresi == defsifre)):
    print ("Sisteme Başarıyla Girdiniz !!!")
elif ((kullaniciadi != defkullaniciadi) and (kullanicisifresi == defsifre)):
    print ("Kullacını Adınız Hatalı Lütfen Tekrar Deneyiniz !")
elif ((kullaniciadi == defkullaniciadi) and (kullanicisifresi != defsifre)):
    print ("Şifreniz Hatalı Lütfen Tekrar Deneyiniz !")
else:
    print ("Bilgileriniz Hatalı Lütfen Tekrar Deneyiniz !")
    