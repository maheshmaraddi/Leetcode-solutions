class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        max=0
        for x in range(k):
            a=min(nums)
            i=nums.index(a)
            # print(a,i)
            nums[i] = (-a)
            # print(nums)
            max=sum(nums)
        return max
            
            
            
            
        