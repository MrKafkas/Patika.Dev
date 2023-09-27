import random
x=1
hak=int(input("Lütfen deneme sayısını giriniz:"))

sayi = random.randint(1,10)


while x <= hak:
    tahmin = int(input("Lütfen bir sayı giriniz:"))
    x += 1
    puan=100-((100/hak)*(x-1))
    if tahmin<sayi:
        print("Tahmininiz Sayıdan Küçüktür.")
    elif tahmin>sayi:
        print ("Tahmininiz Sayıdan Büyüktür.")
    elif tahmin==sayi:
        print("Tebrikler!!! Doğru tahmin, Puanınız:", puan)
        break
    if x>hak:
        print("Haklarınız bitti!!! Tutulan sayı:", sayi)
    
    
