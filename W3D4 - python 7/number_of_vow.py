s = input("Enter the string")

va,ve,vi,vo,vu = 0,0,0,0,0
for ch in s:
    if ch=='a':
        va += 1
    if ch=='e':
        ve+=1
    if ch=='i':
        vi+=1
    if ch=='o':
        vo+=1
    if ch=='u':
        vu+=1
if va !=0 :
    print("Number of a",va)
if ve !=0 :
    print("Number of e",ve)
if vi!=0 :
    print("Number of i",vi)
if vo!=0:
    print("Number of o",vo)
if vu !=0 :
    print("Number of u",vu)
