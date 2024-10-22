def longestSubarray(nums):
    left = 0
    zero_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        # Count the number of zeros in the current window
        if nums[right] == 0:
            zero_count += 1
        
        # If there is more than one zero, shrink the window from the left
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Calculate the length of the current window, subtracting 1 for the deleted element
        max_length = max(max_length, right - left)

    return max_length