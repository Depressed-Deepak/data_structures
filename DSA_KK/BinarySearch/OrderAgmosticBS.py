"""
This code basically check if the given array is 
ascen or descen and give the taget value index acc..
"""

def OrderAgmosticBS(arr, target):
    
    start = 0
    end = len(arr) - 1
    
    # if the starting element > ending element 
    # then boolean is returned
    
    inAsc = arr[start] < arr[end]     
    
    if inAsc:
        while start <= end:
            mid = start + (end - start)//2
            
            if target > arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid -1
            else:
                return mid
        return "Value not Found"
    else:
        while end >= start:
            mid = start + (end - start)//2
            
            if target > arr[mid]:
                end = mid - 1
            elif target < arr[mid]:
                start = mid + 1
            else:
                return mid
        return "Value not Found" 

# a = OrderAgmosticBS([55,44,33,22,11,0], 33)
a = OrderAgmosticBS([-1, 55,78,532,677,789,987,3455,32453], 532)
print(a)