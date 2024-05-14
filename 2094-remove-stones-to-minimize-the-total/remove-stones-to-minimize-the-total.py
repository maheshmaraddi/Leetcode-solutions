import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heapq._heapify_max(piles)
        # print(type(piles))
        while k:
            val = piles[0]
            new = math.floor(val/2)
            piles[0] = val - new
            heapq._siftup_max(piles,0)
            k-=1
        return sum(piles)

        