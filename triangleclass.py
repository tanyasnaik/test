class triangle:
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
def tritype(self):
    a=self.side1
    b=self.side2
    c=self.side3
    if a==b==c:
        print('It is an equilateral triangle!')
    elif a!= b!= c!= a:
        print('It\s a scalene triangle!')
    else:
        print('It is an isosceles triangle!')