class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        if target == 0:
            return len(nums)
        
        if target < 0:
            return -1
        
        current_sum = 0
        left = 0
        min_ops = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                min_ops = min(min_ops, len(nums) - (right - left + 1))
        
        return min_ops if min_ops != float('inf') else -1