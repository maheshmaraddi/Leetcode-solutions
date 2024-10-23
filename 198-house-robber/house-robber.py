class Solution:
    def rob(self, nums):
        # Base cases
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize the dp array
        dp = [0] * len(nums)
        
        # Fill in the base values
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill the dp array using the dynamic programming approach
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # The last element of dp contains the result
        return dp[-1]


