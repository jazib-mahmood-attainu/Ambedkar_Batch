"""
map(para1,para2)

para1: is a function
para2: is a iterable

map returns a map object, that we need to convert into list/tuple/dict

"""

def func(a):
    return a+5

l1 = [0,5,10,15]

l2 = list(map(func,l1))
print(l2)


