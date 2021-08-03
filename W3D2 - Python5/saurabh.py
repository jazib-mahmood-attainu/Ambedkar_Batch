ctr = 0
l = list()
for i in range(1,101):
    if i%2==0:
        
        l.append(i)
# print(l)
j = 0
for i in range(len(l)//3):
    if ctr == 10:
        break
    ctr+=1
    print(l[j])
    j = j+3
    
