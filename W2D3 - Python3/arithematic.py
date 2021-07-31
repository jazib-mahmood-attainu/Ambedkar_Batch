"""
Arithematic/Binary operators:
+ - addition
- - substraction
/ - floating pt division
* - multiplication
// - Integer division
%  - modulus (It gives remainder)
Ctrl+/ - select and comment
** - exponentiation operator

Boolean/comparision operators
==  -   Comparision of equality
>   -   Greater than
>=  -   Greater than or equal to
<   -   Lesser than
<=  -   Lesser than equal to
!=  -   not equal to

Logical operators

and -   And is true, only if left AND right, both are true
Truth Table
Left and right      OUTPUT
T           T          T
T           F          F 
F           T          F
F           F          F

or -    Or is true, when either left is true OR right is true
Left  or right      OUTPUT
T           T          T
T           F          T
F           T          T
F           F          F

not
operator            Output
T                      F
F                      T
"""




a = 5
b = 2
c = 5
str1 = "Sahil"
str2 = "sahil"
str3 = "Sahil"
print("Arithematic ops")
print(a+b) # 7
print(a-b) # 3
print(a/b) # 2.5
print(a*b) # 10
print(a//b) # 2
print(a%b)  # 1 [0 to b-1] => b numbers
print(a**b) # 25
print("Boolean ops")
print(a==b)  # a is 5 and b is 2 - F
print(a==c)  # a is 5 and c is 5 - T   
print(a>b)   # a is 5 and b is 2 - T
print(a>=b)  # a is 5 and b is 2 - T
print(a<b)   # a is 5 and b is 2 - F
print(a<=b)  # a is 5 and b is 2 - F
print(a!=b)  # a is 5 and b is 2 - T
print(a!=c)  # a is 5 and c is 5 - F
print("String comparision")
print(str1==str2) #str1 = "Sahil" ; str2 = "sahil" ; str3 = "Sahil" - F
print(str1==str3) #str1 = "Sahil" ; str2 = "sahil" ; str3 = "Sahil" - T
print(str1!=str2) #str1 = "Sahil" ; str2 = "sahil" ; str3 = "Sahil" - T

print("Logical Operators")
print((a!=b) and (a==c))  # a is 5 and b is 2 and c is 5 - T

print("example")
d = 5
e = 7

print((d==10//2) and (e==5+2) or (d+e==12))
#

print(not (d==e)) # => not False => True


