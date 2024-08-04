class Solution:
    

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod = 10**9 + 7

        # Generate all possible subarray sums
        subarray_sums = []
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                subarray_sums.append(s)

        # Find the sum of elements between 'left' and 'right' using heap
        # Use a min-heap to find the kth smallest element efficiently
        heapq.heapify(subarray_sums)
        result = 0

        for i in range(1, right + 1):
            val = heapq.heappop(subarray_sums)
            if i >= left:
                result += val
                result %= mod

        return result
