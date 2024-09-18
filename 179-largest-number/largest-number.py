class Solution:
    

    
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        print(nums)
        nums.sort(key=lambda x: x * 10, reverse=True)  # Multiply by 10 to compare properly
        print(nums)
        # Join the sorted strings and return
        largest_num = ''.join(nums)
        
        # Remove leading zeros
        largest_num = largest_num.lstrip('0')
        return largest_num if largest_num else '0'
        