def binarySearch(arr, target):

    arr = arr.sort()
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start)//2
        
        if target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid -1
        else:
            return mid
    return "Value not Found"

a = binarySearch([-1, 55,78,532,677,789,987,3455,32453], 44)
print(a)

