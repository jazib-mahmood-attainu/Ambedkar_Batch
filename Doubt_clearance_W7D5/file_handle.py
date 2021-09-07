# """
# Read a file
# """

# file = open("Doubt_clearance_W7D5/dummy.txt",'r')

# # for i in file:
# #     print(i)

# # print(file.read(10))

# # print(file.readlines())

# for i in file.readlines():
#     print(i)

# """
# Write in a file
# """
# f = open("Doubt_clearance_W7D5/temp.txt",'w')
# f.write("ali \n")
# f.write("jazib \n")
# f.close()


# f = open("Doubt_clearance_W7D5/temp.txt",'a')
# f.write("something else")
# f.close()

f = open("Doubt_clearance_W7D5/wall.jpg","rb")
print(f.read())

n = open("Doubt_clearance_W7D5/new.jpg","wb")
for i in f:
    n.write(i)
n.close()

