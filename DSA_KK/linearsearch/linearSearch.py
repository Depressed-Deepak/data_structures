def linearSearch(arr, target):
    length = len(arr)
    
    # when the array is empty, then this condition will run
    if len(arr) == 0:
        return -1
    
    # This is when we check if the target exists in the array 
    # and returning its index
    
    for i in range(length):
        if arr[i] == target:
            return i
    
    # when the item is not found then None is returned 
    return None


a = linearSearch([1,22,4,6,77,43,23], 25 )
print(a)        