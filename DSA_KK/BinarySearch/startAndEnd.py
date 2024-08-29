class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def startEnd(arr, target, is_searching_Left):
            start = 0
            end = len(arr) - 1
            index = -1
            
            while start <= end:
                mid = start + (end - start) // 2
                if arr[mid] < target:
                    start = mid + 1
                elif arr[mid] >  target:
                    end = mid - 1
                else:
                    index = mid
                    if is_searching_Left:
                        end = mid - 1
                    else:
                        start = mid + 1
            return index

        start = startEnd(nums, target , True)
        end = startEnd(nums, target, False)

        return [start, end]

'''
                BRUTEFORCE METHOD
    starting = ''
    ending = ''
    for i in range(end):       
        if arr[i] == target:
            starting = i
            break
    
    for i in range(end, 0, -1):
        print(i)
        if arr[i] == target:
            ending = i
            break
    return [starting, ending]
'''   