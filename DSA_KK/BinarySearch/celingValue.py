# this question returns target value or the celing value of target in an arrar
# celing value= value greater than the next value of the target

def celingValue(arr, target):
    
    start = 0
    end = len(arr) - 1
    
    if target > arr[end]:
        return "No value is greater than the target value"
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] > target:
            end = mid - 1
            
        else:
            start = mid + 1
    return start



a = celingValue([-1, 55,78,532,677,789,987,3455,32453], 345)
print(a)
