class Solution:

    def maxWealth(self, account):
        ans = 0
        # account is a 2d array i.e account[][]
        # coustomer is row 
        # wealth is column
        
        for customer in account:
            total_sum = 0
            # a row is a list for column
            for wealth in customer:
                total_sum = total_sum + wealth
            
            if total_sum > ans:
                ans = total_sum
        return ans
solution = Solution()
a = solution.maxWealth( [[1, 100, 3], [4, 5, 6], [7, 8, 9]] )
print(a)