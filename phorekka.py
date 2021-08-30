nums = [1,1,2,2,2,3,3]

def frequencySort(nums):
    nums.sort(reverse=True)
    my_dict = dict()
    A = list()

    for i in nums:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1
    print(my_dict)

    # sort a dictionary
    # dic2 = dict(sorted(my_dict.items(), key=lambda item: item[0]))
    # print(dic2)
    dic1 = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    print(dic1)

    l = []

    for k,v in dic1.items():
        for i in range(v):
            l.append(k)

    return l


print(frequencySort(nums)) 