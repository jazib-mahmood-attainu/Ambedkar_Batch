"""
when we declare a variable, it is stored inside ram.

list are contiguous/adjacent memory cells in ram, thta we can use using it's index.
Index always starts from zero.

if n elements are there, it's indices will be 0 to n-1
eg: n = 7 elements
indices will be zero to 6

range(5)-> [0,1,2,3,4]

API - application programming interface(functions we can use on something, here something is a list)

len()
len(<list>)= length of that list

list_name[idx] is used to access element at index idx in list list_name
"""

# A = []
# A = list()
# A = [1,2,3,4,5,6,7]

fruits = ["Apple","Banana","Papaya"]

print(fruits)
print(type(fruits))
print(len(fruits))

print(fruits[1])



