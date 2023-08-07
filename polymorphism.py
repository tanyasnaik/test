class car:
    def __init__(self,name,mileage):
        self._name=name
        self.mileage=mileage

    def descrip(self):
        print(f'The {self._name} gives {self.mileage}')


class BMW:
    def __init__(self,series):
        self.series=series

    def descrip(self):
        print(self.series)

obj1=car('Audi',25)
obj2=BMW('Z series')
obj1.descrip()
obj2.descrip()