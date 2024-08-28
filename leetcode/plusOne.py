def arrayPlusOne(arr):
    # Convert list of digits to a single integer
    num = int(''.join(map(str, arr)))
    
    # Add 1 to the integer
    num += 1
    
    # Convert the resulting number back to a list of digits
    result = [int(digit) for digit in str(num)]
    
    return result

# Example usage
result = arrayPlusOne([1, 2, 3, 4])
print(result)  # Output: [1, 2, 3, 5]
