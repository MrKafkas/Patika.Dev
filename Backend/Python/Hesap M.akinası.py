giriş="""
(1)topla
(2)çıkar
(3)çarp
(4)böl
(5)karesini hesapla
(6)karekök hesapla
"""
print(giriş)

while True:
    soru=input("Yapmak istediğiniz işlemi seçiniz (çıkış için q):")
    if soru=="q":
        print("Çıkılıyor")
        break
    
    elif soru=="1":
        sayı1=int(input("Toplama işlemi için ilk sayıyı girin:"))
        sayı2=int(input("Toplama işlemi için ikinci sayıyı girin"))
        print(sayı1,"+",sayı2,"=",sayı1+sayı2)
    elif soru=="2":
        sayı3=int(input("Çıkarma işlemi için ilk sayıyı girin:"))
        sayı4=int(input("Çıkarma işlemi için ikinci sayıyı girin:"))
        print(sayı3,"-",sayı4,"=",sayı3-sayı4)
    elif soru=="3":
        sayı5=int(input("çarpmak istediğiniz ilk sayıyı giriniz:"))
        sayı6=int(input("çarpmak istediğiniz ikinci sayıyı giriniz:"))
        print(sayı5,"*",sayı6,"=",sayı5*sayı6)
    elif soru=="4":
        sayı7=int(input("bölmek istediğiniz ilk sayıyı giriniz:"))
        sayı8=int(input("bölmek istediğiniz ikinci sayıyı giriniz"))
        print(sayı7,"/",sayı8,"=",sayı7/sayı8)
    elif soru=="5":
        sayı9=int(input("karesini hesaplayacağınız sayıyı giriniz:"))
        print(sayı9**2)
    elif soru=="10":
        sayı10=int(input("Karekökünü almak istediğiniz sayıyı giriniz:"))
        print(sayı10**0.5)
    else:
        print("Yanlış giriş")
        print("Aşağıdaki seçeneklerden birini giriniz:",giriş)
    
    
                  
