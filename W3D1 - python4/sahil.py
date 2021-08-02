# n =  int(input("Enter a number"))

# c = 0
# for i in range(1,n):
#     if n%i==0:
#         c=c+1
 
# print(c)
# if c>1:
#     print("not prime")
# else:
#     print("prime")

def sp(word) : 
    # return word[0:2]+'... '+word[0:2]+'... '+word+'?' 
    print("'{0}{1}{2}{3}{4}{5}'".format(word[0:2],"... ",word[0:2],"... ",word,"?")) 
sp("hello")