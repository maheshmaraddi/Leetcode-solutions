from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Initialize dp array with -1
        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]
        
        # Base case: An empty subsequence has a sum of 0 and length 0
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(1, n + 1):
            for t in range(target + 1):
                # If we don't include the current element nums[i-1]
                dp[i][t] = dp[i-1][t]
                
                # If we include the current element nums[i-1]
                if t >= nums[i-1] and dp[i-1][t-nums[i-1]] != -1:
                    dp[i][t] = max(dp[i][t], dp[i-1][t-nums[i-1]] + 1)
        
        return dp[n][target]

# # Example usage:
# sol = Solution()
# nums = [1, 2, 3, 4, 5]
# target = 10
# result = sol.lengthOfLongestSubsequence(nums, target)
# print("Length of the longest subsequence with sum equal to target:", result)
