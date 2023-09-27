kullanici_adi=input("Kullanıcı Adı:")
parola=input("Parola:")

if kullanici_adi=="mrkfks" and parola=="S5s5mrkfks":
    print(kullanici_adi,"Hoşgeldiniz")
    bool(parola)
    
else:
    print("Kullanıcı Adı veya Parola Hatalı!")

maas=float(input("Aylık Ücretiniz:"))
ek_odeme=float(input("Terör Tazimnatınız:"))
promosyon=float(input("Banka Promosyon Ücretiniz:"))
izin=float(input("İzin Kullandığınız Gün Sayısı:"))

calisilan_gun=30-izin
tazminat=(ek_odeme/30)*calisilan_gun
print(maas+ek_odeme+promosyon+tazminat)



