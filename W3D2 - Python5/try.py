n = int(input("Enter a number :")) 
total = 0 
for i in range(1, n + 1): 
    total += i print(i , end = '') if i == n: print(end = '') else: print(' + ', end = '') print(' = ', total, end = '') 