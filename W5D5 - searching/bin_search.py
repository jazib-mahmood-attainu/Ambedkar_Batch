arr = [1,23,45,56,65,78,85,98]

target = 99

def bin_search(arr,x):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2

        #if x is greater than middle number,ignore left half
        if arr[mid]<x:
            low = mid+1

        #if x is smaller than middle number,ignore right half
        elif arr[mid]>x:
            high = mid - 1

        else:
            return mid

    return -1


if __name__=="__main__":
    res = bin_search(arr,target)

    if res == -1:
        print("Target not present")
    else:
        print("Element is present at index",res)



