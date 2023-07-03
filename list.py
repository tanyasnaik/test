fruits = ['apple', 'banana', 'kiwi', 'orange', 'watermelon', 'mango', 'pineapple']

fruits.append('grapes')

fruits.remove('mango')
fruits.pop()
del fruits[3]

#del fruits 
fruits.clear()

for x in fruits:
    print(x)

print(len(fruits[0]))