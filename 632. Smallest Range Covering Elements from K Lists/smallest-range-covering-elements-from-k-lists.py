import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        
        # Initialize the heap and the current maximum
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))  # (value, list index, element index)
            current_max = max(current_max, nums[i][0])
        
        smallest_range = float('inf')
        range_start, range_end = 0, 0
        
        while min_heap:
            current_min, list_index, element_index = heapq.heappop(min_heap)

            # Update the smallest range found
            if current_max - current_min < smallest_range:
                smallest_range = current_max - current_min
                range_start, range_end = current_min, current_max
            
            # If there are more elements in the current list, push the next element to the heap
            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                current_max = max(current_max, next_value)
            else:
                # If we can't push more elements, we are done
                break
        
        return [range_start, range_end]
