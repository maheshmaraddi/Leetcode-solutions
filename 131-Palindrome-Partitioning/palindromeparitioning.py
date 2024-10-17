from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current_partition = []

        def backtrack(start):
            # If we have reached the end of the string, store the current partition
            if start >= len(s):
                result.append(current_partition[:])
                return
            
            for end in range(start, len(s)):
                # Check if the substring s[start:end+1] is a palindrome
                if is_palindrome(s, start, end):
                    # Add the palindrome to the current partition
                    current_partition.append(s[start:end+1])
                    # Recur for the next part of the string
                    backtrack(end + 1)
                    # Backtrack by removing the last added palindrome
                    current_partition.pop()

        # Helper function to check if a substring is a palindrome
        def is_palindrome(substring, left, right):
            while left < right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            return True

        # Start the backtracking process
        backtrack(0)
        return result

# Example usage:
solution = Solution()
print(solution.partition("aab"))
