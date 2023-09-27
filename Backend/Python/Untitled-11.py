#a=int(input("Bir Sayı Giriniz:"))
#x=(a>0 and a<100)==True 
#print(f"Girdiğiniz {a} sayısı 0 ile 100 arasında mı?.", (x))

#a=int(input("Bir sayı giriniz:"))
#x=(a>0 and a%2==0)==True
#print(f"Girdiğiniz {a} sayısı pozitif çift sayı mı?:", (x))

from calendar import c


a=int(input("İlk sayıyı giriniz:"))
b=int(input("İkinci sayıyı giriniz:"))
c=int(input("Üçüncü sayıyı giriniz:"))
list=[a, b, c].sort()
print("Girilen sayıların büyükten küçüğe sırası:", list)