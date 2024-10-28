def subsets(nums):
    result = []

    def backtrack(start, subset):
        # Add the current subset to the result
        result.append(subset[:])
        
        # Explore further by including each number after the current start position
        for i in range(start, len(nums)):
            # Include nums[i] in the subset
            subset.append(nums[i])
            # Move on to the next element
            backtrack(i + 1, subset)
            # Backtrack: remove nums[i] from the subset
            subset.pop()
    
    # Start the backtracking with an empty subset
    backtrack(0, [])
    return result
