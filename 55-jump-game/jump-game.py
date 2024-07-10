class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0 
        maxreach =0
        n=len(nums)
        while i<n and i<=maxreach:
            maxreach = max(maxreach, i+nums[i])
            i+=1
        return i==n
                    