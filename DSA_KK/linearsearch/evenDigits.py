# return the total number of a list where a element has
# even number of digits
# input : [1,24,345,67,8888,88]
# output: 4 because in the array there are four numbers which has even digits




def evenDigits(arr):
    
    count = 0
    for num in arr:
        if even(num):
            count += 1
    return count

# def even(num):
#     a = digits(num)
#     if a % 2 == 0:
#         return True

# def digits(num):
#     counter = 0
#     while num > 0:
#         counter += 1
#         num =  num / 10
#     return counter


def even(num):  
    counter = 0
    while num > 0:
        num = num / 10
        counter += 1
    return counter % 2 == 0
    

a = evenDigits([1,24,345,67,8888,88])
print(a)



    