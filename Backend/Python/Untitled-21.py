# class Person:
#     adress='No İnfomation'
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year
#     def intro(self):
#         print('Hello there. I am'+ self.name)
#     def calculateAge(self):
#         return 2022-self.year

# p1=Person(name='ali', year=1990)
# p2=Person(name='veli', year=1980)

# p1.intro()
# p2.intro()

# print(f'adım:{p1.name} ve yaşım:{p1.calculateAge()}')
# print(f'adım {p1.name} ve yaşım:{p1.calculateAge()}')

# class Circle:
#     pi=3.14
#     def __init__(self,yaricap=1):
#         self.yaricap=yaricap
#     def cevre_hesapla(self):
#         return 2*(self.pi*self.yaricap)
#     def alan_hesapla(self):
#         return self.pi*(self.yaricap**2)

# c1=Circle()
# c2=Circle(5)

# print(f'c1: alan={c1.alan_hesapla()}, çevre={c1.cevre_hesapla()}')
# print(f'c2: alan={c2.alan_hesapla()}, çevre={c2.cevre_hesapla()}')