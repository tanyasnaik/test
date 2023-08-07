class car:
    def __init__(self,name,mileage):
        self.name=name
        self.mileage=mileage
    def descrip(self):
        print(f'The {self.name} gives {self.mileage}')

class BMW(car):
    pass

class Audi(car):
    def descrip(self): #method overriding , operator overriding
        print('This is the Audi class description')
        super().descrip()
    def printvalue(self):
        print('Audi class')

obj1=BMW('BMW 7-series',30.43)
obj1.descrip()

obj2=Audi('Audi L',49.1)
obj2.descrip()
obj2.printvalue()
