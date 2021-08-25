def reverse(string):
    if len(string)==0:
        return
    print (string[-1],end="")
    reverse(string[:-1])
    

string = "sentence"
reverse(string)
print()
