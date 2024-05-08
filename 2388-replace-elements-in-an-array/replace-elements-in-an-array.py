class Solution:
    def arrayChange(self, nums: List[int], op: List[List[int]]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums)}
        
        for a, b in op:
            idx = index_map[a]
            nums[idx] = b
            del index_map[a]
            index_map[b] = idx
        return nums
        