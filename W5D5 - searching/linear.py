arr = [1,23,45,65,98,78,23,56,85]

target = 85

def linear_search(arr,x):
    for i in arr:
        if i == x:
            print("present")
            return
    print("not present")


if __name__=="__main__":
    linear_search(arr,target)