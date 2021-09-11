l = [1,2,1,1,1,2,3,4,5,5]

f_dict = dict() #{}

for i in l:
    if i not in f_dict:
        f_dict[i] = 1
    else:
        f_dict[i] += 1

print(f_dict)
