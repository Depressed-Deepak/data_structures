def findMax(arr):
    if len(arr) == 0:
        return -1
    
    ans = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > ans:
            ans = arr[i]
    return ans

max = findMax([1,23,5,3,34,36,120])
print("The maximum value is ", max)

def findMix(arr):
    if len(arr) == 0:
        return -1
    
    ans = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < ans:
            ans = arr[i]
    return ans

max = findMix([1,23,5,3,0,36,120])
print("The minimum value is ", max)