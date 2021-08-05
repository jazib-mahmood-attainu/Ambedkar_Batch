x = 50 
def func(y):
    global x 
    print('x is', y) 
    x = 2 
    print('Changed local x to', x) 
func(x) 
print('x is now', x)