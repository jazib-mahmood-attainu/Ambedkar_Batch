"""
scope - availability of a variable

def ABC():
    sum = 10
    for i in range(10):
        sum = 0
    print(sum)

"""

# sum = 5                                     #global variable
# def ABC():
#     sum = 10                                #local variable
#     # print("value of sum inside the function is ",sum)

# ABC()

# print(sum)

x = 50 #global
def func(x):
    print('x is', x)
    x = 2#local
    print('Changed local x to', x)
func(x)
print('x is now', x) 