class animal:
    name='Dog'
    def __init__(self,colour,breed):
        self.colour=colour
        self.breed=breed
    def print_values(self):
        print('I have a',self.name) 
        print('Its colour is',self.colour)
        print('Its breed is',self.breed)


Roger=animal('Black','pug')
print(Roger.name)
print(Roger.colour)
Roger.print_values()
