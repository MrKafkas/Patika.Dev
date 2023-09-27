isim = input("İsminiz nedir? ")
print("Merhaba", isim, end="!\n")


maas_odemesi=float(input("Aylık Ücretiniz nedir?"))
ek_odeme=float(input ("Aylık ek ödemeniz nedir?"))
promosyon_odemesi=float(input("Aylık promosyon ödemeniz nedir?"))
enflasyon_orani=float(input("Enflasyon oranı nedir?"))

artis=enflasyon_orani*(maas_odemesi + ek_odeme)

maas_artisi=artis+promosyon_odemesi

zamlı_maas=maas_odemesi + ek_odeme + maas_artisi

print("-"*30)
print("Maaş Ödemesi\t:", maas_odemesi)
print("Ek Ödeme\t:", ek_odeme)
print("Promosyon\t:", promosyon_odemesi)
print("Maaş Artışı\t:", maas_artisi)
print("-"*30)
print("Yeni Zamlı Maaş\t:", zamlı_maas)






