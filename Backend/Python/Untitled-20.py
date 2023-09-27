class Circle:
    
    pi=3.14
    
    def __init__(self,yaricap=1):
        self.yaricap=yaricap
    def cevre_hesapla(self):
        return 2*(self.pi * self.yaricap)
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    
c1=Circle()
c2=Circle(5)

print(f'c1:Alan={c1.alan_hesapla()}, Çevre={c1.cevre_hesapla}')
print(f'c2:Alan={c2.alan_hesapla()}, Çevre={c2.cevre_hesapla}')