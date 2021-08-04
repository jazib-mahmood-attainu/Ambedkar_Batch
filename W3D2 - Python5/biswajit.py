a = int(input()) 
b = int(input()) 
c = int(input()) 
if a>b or a>c: 
    if a<b or a<c: 
        print(a) 
elif b>a or b>c: 
    if b<a or b<c: 
        print(b) 
else : print(c) 