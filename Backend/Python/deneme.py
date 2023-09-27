while True:
    ilk_sayı=input("ilk sayı(Programdan çıkmak için q tuşuna basın):")
    if ilk_sayı=="q":
        print("Programdan Çıkılıyor...")
        break    
    ikinci_sayı=input("ikinci sayı:")
try:
    sayı1=int(ilk_sayı)
    sayı2=int(ikinci_sayı)
    print(sayı1,"/",sayı2,"=",sayı1/sayı2)
except (ValueError) as hata:
    print("Bir hatayla Karşılaşıldı",hata)
else:
    try:
        print(bölünen/bölen)
    except ZeroDivisionError:
        print("Bir sayıyı sıfıra bölemezsin!")
