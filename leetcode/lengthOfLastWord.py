def lengthOfLastWord(s):
    
    end = len(s) - 1
    
    while s[end] == " ":
        end -= 1
    
    start = end
    while start >= 0 and s[start] != " ":
        start -= 1
    
    return end - start

print(lengthOfLastWord("  The moon is very   kirey "))