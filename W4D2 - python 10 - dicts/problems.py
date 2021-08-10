"""
len(list_name) = number of elements in the list

Q - print Hello <element> for all the elements

Q - 

"""
names = ["Praveen","Ankit", "Amar","Ali","Phorekka"]
#           0       1           2   3       4

for i in names:
    print("Hello", i)

print("other way===========================")

for i in range(len(names)): # [0,1,2,3,4]
    print("Hello", names[i])


print("Using while===========================")

n = len(names)
i = 0
while(i<n):
    print("Hello", names[i])
    i+=1

