print ("Garenin Haremi Sistemlerine Hoşgeldiniz!")
defkullaniciadi=("Baba yak")
defsifre=("12345")
while (True):
    kullanici=input("Kullanıcı Adınızı Giriniz: ")
    sifre=input("Şifrenizi Giriniz: ")
    if ((kullanici == defkullaniciadi) and (sifre == defsifre)):
        print ("Sisteme Başarıyla Girdiniz !!!")
        break
    elif ((kullanici != defkullaniciadi) and (sifre == defsifre)):
        print ("Kullanıcı Adınızı Hatalı Girdiniz Lütfen Tekrar Deneyiniz !")
    elif ((kullanici == defkullaniciadi) and (sifre != defsifre)):
        print("Şifrenizimi Unuttunuz?")
        print("Şifrenizi Değiştirmek İster Misiniz? E/H")
        cevap=input()
        if (cevap == "E"):
            yeniparola=input("Yeni Şifrenizi Giriniz! ")
            print ("Lütfen Bekleyiniz")
            defsifre=yeniparola
            print("Şifreniz Başarıyla Değiştirilmiştir !")
    else:
        print("Lütfen Tekrar Deneyiniz !")
        if ((kullanici != defkullaniciadi) and (sifre != defsifre)):
            print ("Girdiğiniz Kullanıcı Adı Ve Şifreyle Hesap Bulunmamaktadır Lütfen Tekrar Deneyiniz !")