def searchInsert(arr, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    start = 0
    end = len(arr)-1
    
    
    while start <= end:
        mid = (end + start) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1 
    return start

a = searchInsert([1,5,8,18,23], 9)
print(a)
            
    