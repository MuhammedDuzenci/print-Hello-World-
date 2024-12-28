print("Sezar Şifreleme Sistemine Hoşgeldiniz !")
def sezar(metin,kaydirma):
    sifrelenmismetin=""
    for karakter in metin:
        if karakter.isalpha():
            if karakter.isupper():
                sifrelenmismetin += chr((ord(karakter) - 65 + kaydirma) % 26 + 65)
            else:
                sifrelenmismetin += chr((ord(karakter) - 97 + kaydirma)% 26 + 97)
        else:
            sifrelenmismetin += karakter
    return sifrelenmismetin

metin=(input("Şifrelemek İsteğiniz Metini Giriniz: "))
kaydirma=int(input("Lütfen Kaydırmak İstediginiz Miktarı Yazınız: "))

sifrelenmismetin=sezar(metin,kaydirma)
print(f"Şifrelenmiş Metin:{sifrelenmismetin}")