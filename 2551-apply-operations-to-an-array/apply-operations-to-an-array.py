class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        zero = nums.count(0)
        while 0  in nums:
            nums.remove(0)
        for i in range(zero):
            nums.append(0)
        return nums