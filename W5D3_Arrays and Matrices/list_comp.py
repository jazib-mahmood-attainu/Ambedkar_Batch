"""
list comprehension is a shortcut way to make a list
"""

l1 = []
n = 5

for i in range(n):
    l1.append(i)

print(l1)

#Short hand operation
m = 5
l2 = [i for i in range(m)]
print(l2)