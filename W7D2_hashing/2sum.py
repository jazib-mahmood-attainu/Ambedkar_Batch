# # A = [2,3,4,1,6]
# # def solve(A):
# #     A.sort() #merge sort -> nlogn
# #     # A = [1,2,3,4,6]
# #     #        l     h

# #     l = 0
# #     h = len(A)-1

# #     target = 9

# #     while l<h:
# #         s = A[l]+A[h]
# #         if s > target:
# #             h-=1
# #         elif s < target:
# #             l+=1
# #         else:
# #             return True
    
# #     return False

# # print(solve(A))

# class Solution:
#     def twoSum(self, nums, target):
#         hash_table = dict()
        
#         n = len(nums)
        
#         for i in range(n):
#             temp = target - nums[i]
#             if temp in hash_table:
#                 return [hash_table[temp],i]
#             else:
#                 hash_table[nums[i]] = i
# A = [2,3,4,1,6]
# #    0 1 2 3 4
# obj = Solution()
# res = obj.twoSum(A,target = 9)
# print(res)

l = [10,20,30,5,10,50] 
sum = l[0] 
m = l[0] 
l1 = [] 
l1.append(l[0]) 
for i in range(1,len(l)): 
    
    if m < l[i]: 
        sum += l[i] 
        m = l[i] 
        l1.append(sum) 
    else: 
        l1.append(l[i]) 
        m = l[i] 
        sum = l[i] 
print(l1) 
print(max(l1)) 
# print(m)