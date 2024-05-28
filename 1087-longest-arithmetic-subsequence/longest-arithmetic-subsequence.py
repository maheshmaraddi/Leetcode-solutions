class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        max_length = 1
        
        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                dp[j][diff] = dp[i][diff] + 1
                max_length = max(max_length, dp[j][diff])
        
        return max_length
        