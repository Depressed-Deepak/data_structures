def linearSearch(str , char ):
    
    # This happens when string is not provided
    if len(str) == 0:
        return -1
    
    for i in range(len(str)):
        if str[i] == char:
            return i
    # if the character is not found in the string 
    # after completing the loop this happens
    return "Character is not available"

a = linearSearch("This is Deepak", 'e')
print(a)

"""
When you want to change the range of i in the for loop
syntax:
for i in range(4, 10)

"""


    