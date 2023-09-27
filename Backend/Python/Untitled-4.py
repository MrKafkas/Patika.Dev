message = "Hello There. My name is Ömer KAFKAS."
#message = message.upper() #bütün karakterleri büyük yapar.
#message = message.lower() #bütün karakterleri küçük yapar. 
#message = message.title() #kelimelerin ilk karakterlerini büyük yapar.
#message = message.capitalize() #stringin ilk karakterini büyük yapar.
#message = message.strip()   #string ifadenin en başında boşluk varsa boşluğu siler
#message = message.split()   #ifadeyi kelimelere ayırıp her kelime üzerinde ayrı ayrı işlem yapılmasına izin verir.
#message = ''.join(message) #ayrılmış ifadeyi birleştirir.
#print(message)

#isFound = message.startswith("T")
#isFound = message.endswith("S")
#print(isFound)

#message = message.replace("hello","Merhaba").replace("Ömer","Göktuğ").replace("There","Herkese")
message = message.center(100,'*')
print(message)




#index = message.find('KAFKAS')
#print(index)

