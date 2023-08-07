class car:
    def __init__(self,name,mileage):
        self._name=name
        self.mileage=mileage

    def description(self):
        print(f'The {self._name} gives {self.mileage} kmph')


obj2=car('Audi',23)
print(obj2._name)
obj2.description()