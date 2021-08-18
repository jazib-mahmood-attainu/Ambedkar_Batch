"""
join function joins all string elements from a list into a single string
Syntax:
"<separator>".join(list/tuple/dict)
"""

l = ["a","b","c","d","e"]

res = "".join(l)
print(res)

res = " ".join(l)
print(res)

res = "%".join(l)
print(res)
