# Python3 code to demonstrate working of
# Getting first key in dictionary
# Using keys() + list()

# initializing dictionary
test_dict = {'Gfg': 1, 'is': 2, 'best': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using keys() + list()
# Getting first key in dictionary
res = list(test_dict.keys())[0]

# printing initial key
print("The first key of dictionary is : " + str(res))
