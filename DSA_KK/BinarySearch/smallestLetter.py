# this question returns target value or the celing value of target in an arrar
# celing value= value greater than the next value of the target

def celingValue(letters, target):
    
    start = 0
    end = len(letters) - 1
    
    if target > letters[end]:
        return "No value is greater than the target value"
    while start <= end:
        mid = start + (end - start) // 2
        
        if letters[mid] > target:
            end = mid - 1   
        else:
            start = mid + 1
    return letters[start % len(letters)]

a = celingValue(['f','h','j','m','n','z'], 'a')
print(a)
