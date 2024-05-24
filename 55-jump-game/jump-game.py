class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # maximum index reachable from current position

        for i, num in enumerate(nums):
            # If the current index is unreachable, return False
            if i > max_reachable:
                return False
            
            # Update the maximum reachable index if needed
            max_reachable = max(max_reachable, i + num)

            # If the last index is reachable, return True
            if max_reachable >= len(nums) - 1:
                return True

        return False
        