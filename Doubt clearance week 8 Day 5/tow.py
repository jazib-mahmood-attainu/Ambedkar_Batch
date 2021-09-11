
def toH(n,S,D,E):
    if n==1:
        print("move from S to D")
        return
    toH(n-1,S,E,D)
    print("Move S to D")
    toH(n-1,E,D,S)

n = 25
toH(n,"Source","Dest","Extra")
