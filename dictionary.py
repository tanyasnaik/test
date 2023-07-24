fruits = {
    'Apple' : 'Red',
    'Banana' : 'Yellow',
    'Watermelon' : 'Green'
}

print(fruits['Watermelon'])

fruits['Watermelon'] = 'Red'
print(fruits['Watermelon'])

fruits['Grapes'] = 'Green'
print(fruits)

del fruits['Apple']
print(fruits)

for i in fruits:
    print(i, ' : ',fruits[i])

for i in fruits.values():
    print(i)

for x,y in fruits.items():
    print(x,y)

print(len(fruits))

if 'Banana' in fruits:
    print('Banana is there!')
else:
    print('Banana isn\'t there.')

fruits.pop('Watermelon')
print(fruits)

fruits.popitem()
print(fruits)

fruitcopy=fruits.copy()
print(fruitcopy)
newfruit=dict(fruits)
print(newfruit)