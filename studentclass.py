class student:
    def __init__(self,name,grade,age):
        self.name=name
        self.grade=grade
        self.age=age
    def print_value(self):
        print('My name is',self.name)
        print('I am studying in Class',self.grade)
        print('I am',self.age,'years.')

student1=student('Tanya',9,14)
student1.print_value()


#name,grade,age