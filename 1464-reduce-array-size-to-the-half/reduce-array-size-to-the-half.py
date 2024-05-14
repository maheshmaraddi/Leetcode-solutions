from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 2:
            return 1
        
        # Count frequencies of elements
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Sort frequencies in descending order
        sorted_freq = sorted(freq_map.values(), reverse=True)
        
        # Find minimum set size
        half_n = n // 2
        count = 0
        sum_freq = 0
        for freq in sorted_freq:
            sum_freq += freq
            count += 1
            if sum_freq >= half_n:
                break
        
        return count
