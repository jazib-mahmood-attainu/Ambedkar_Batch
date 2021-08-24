def add(a,b):
    if a>=100:
        return 
    c = a+b
    print(c)
    add(a+1,b)
    return c


add(2,3)