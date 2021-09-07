a = 5
b = 3

b5 = bin(5)[2:]
b3 = bin(3)[2:]

l5 = len(b5)
l3 = len(b3)

if l5>l3:
    d = l5-l3
    
    while d > 0:
        b3 = '0'+  b3
        d-=1
else:
    d = l3-l5
    b5 = b5
    while d > 0:
        b5 = '0'+  b5
        d-=1
print(b3,b5)    
r = []
for i in range(len(b5)):
    r.append(str(int(b5[i])^int(b3[i])))

r2 = "".join(r)

print(r2)

