"""
q - 1 finding frquency of each element
q - 2 which party won?
"""

# A = [1,2,1,1,1,2,3,4,5,5]
# # 1->4  2->2    3->1    4->1    5->2

# freq = {}

# for ele in A:
#     if ele not in freq:
#         freq[ele] = 1
#     else:
#         freq[ele] += 1

# print(freq)


parties = ["BJP","Congress","BJP","AAP","Congress","AAP","BJP","AAP","AAP"]

freq = dict()

for party in parties:
    if party not in freq:
        freq[party] = 1
    else:
        freq[party] += 1

print(freq)
print(freq.keys())
print(freq.values())
for key in freq.keys():
    print(freq[key])

for val in freq.values():
    print(val)


a = {1,2,3}
b = {3,"d","e"}
print(a-b)
print(a.intersection(b))

x = ["apple", "banana", "cherry"]

del x[0]

print(x)