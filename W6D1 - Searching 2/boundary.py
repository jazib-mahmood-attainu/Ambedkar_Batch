def lower_bound(A,target):
    low = 0
    high = len(A)-1

    ans = -1

    while (low<=high):
        mid = (low+high)//2
        if A[mid]==target:
            ans = mid
            high = mid-1    
        elif (A[mid]>target):
            high = mid - 1
        elif (A[mid]<target):
            low = mid+1

    return ans

def upper_bound(A,target):
    low = 0
    high = len(A)-1

    ans = -1

    while (low<=high):
        mid = (low+high)//2
        if A[mid]==target:
            ans = mid
            low = mid+1
        elif (A[mid]>target):
            high = mid - 1
        elif (A[mid]<target):
            low = mid+1

    return ans


if __name__=="__main__":
#index   0 1 2 3 4 5 6
    A = [1,2,2,2,2,2,2,3,3,3,4,4,4]
    res_l = lower_bound(A,2)
    res_u = upper_bound(A,2)
    if res_l == -1:
        print("No not present")
    else:
        print("Lower bound",res_l)

    if res_u == -1:
        print("No not present")
    else:
        print("Upper bound",res_u)


    print("Number of target number in the list",res_u-res_l+1)