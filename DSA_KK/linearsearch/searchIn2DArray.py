def search2d(arr, target):
    if len(arr) == 0:
        return -1
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == target:
                return [i , j]
            
    return "Item not found"

a = search2d( [[1, 2, 3], [4, 5, 6], [7, 8, 9]] , 9)
print(a)