def evenDigits(arr):
    
    count = len(arr) - 1
    for i in range(len(arr)):
        if len(str(arr[i])) % 2 != 0:
            arr.remove(arr[i])
            count -= 1
            
    return count

# def changeToString(arr):
#     for i in range(len(arr)):
#         arr[i] = str(arr[i])
#     return arr

def countDigits(arr):
    while arr[i] > 0:
        arr[i] = arr[i]/10
            
            
    return arr


a = countDigits([1,33,24,345,67,8888])
print(a)
    