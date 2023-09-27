#name=input("İsminiz:")
#age=int(input("Yaşınız:"))
#edu=input("Eğitim Drumunuz:")

#if (edu=="Lise" or "Üniversite") and (age>18):
    #print("Ehliyet Alabilirsiniz.")
#else:
    #print("Ehliyet alamazsınız.")

#a=float(input("İlk Yazılı Notu:"))
#b=float(input("İkinci Yazılı Notu"))
#c=float(input("Sözlü Notu"))
#ort=(a + b + c)/3

#if 0<ort<24:
    #print("Not Bilginiz:0")
#elif 25<ort<44:
    #print("Not Bilginiz:1")
#elif 45<ort<54:
    #print("Not Bilginiz:2")
#elif 55<ort<69:
    #print("Not Bilginiz:3")
#elif 70<ort<84:
    #print("Not Bilginiz:4")
#elif 85<ort<100:
    #print("Not Bilginiz:5")
#else:
    #print("Hatalı Giriş Yaptınız...")

#import datetime

#tarih=input("Aracınız hangi tarihte trafiğe çıktı (2019/8/9):")

#tarih=tarih.split('/')

#trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
#simdi=datetime.datetime.now()

#fark=simdi-trafigecikis
#days=fark.days


#if days <= 365 :
    #print("1. Servis aralığı.")

#elif 365 < days <= 365*2 :
    #print("2. Servis aralığı.")

#elif 365*2 < days <= 365*3 :
    #print("3. Servis aralığı.")

#else:
    #print("hatalı süre.")