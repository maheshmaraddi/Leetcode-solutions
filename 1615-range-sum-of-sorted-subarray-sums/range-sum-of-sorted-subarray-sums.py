class Solution:
    

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7
        
        # Calculate prefix sums
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
        # Generate all possible subarray sums
        subarray_sums = []
        for i in range(n):
            for j in range(i + 1, n + 1):
                subarray_sums.append(prefix_sums[j] - prefix_sums[i])
        
        # Sort the subarray sums
        subarray_sums.sort()
        
        # Calculate the sum of the elements from 'left' to 'right'
        result = sum(subarray_sums[left - 1:right]) % mod
        
        return result
