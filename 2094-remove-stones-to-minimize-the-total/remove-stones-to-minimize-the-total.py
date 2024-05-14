import heapq
import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Create a max heap from the negative values of the piles
        max_heap = [-x for x in piles]
        heapq.heapify(max_heap)
        
        # Perform k operations
        while k:
            # Fetch the maximum value from the heap
            max_val = -heapq.heappop(max_heap)
            # Calculate the new value after operation
            new_val = max_val - math.floor(max_val / 2)
            # Push the new value back to the heap
            heapq.heappush(max_heap, -new_val)
            k -= 1
        
        # Calculate the sum of remaining values in the heap
        return sum(-x for x in max_heap)
