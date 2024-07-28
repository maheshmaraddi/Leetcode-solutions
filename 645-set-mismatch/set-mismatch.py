class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num)-1] < 0: res.append(abs(num))
            nums[abs(num)-1] *= -1
        for i, num in enumerate(nums):
            if num > 0 and i+1 != res[0]: res.append(i+1)
        return res