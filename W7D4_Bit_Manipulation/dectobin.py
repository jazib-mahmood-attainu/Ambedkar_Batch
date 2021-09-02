def dectobin(dec):
    binary = ""
    while dec>0:
        rem = dec%2
        binary = binary + str(rem)
        dec //=2

    return binary[::-1]

print(dectobin(31))