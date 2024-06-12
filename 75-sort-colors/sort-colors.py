class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        nums.clear()
        if 0 in d:
            while (d[0]):
                nums.append(0)
                d[0]-=1
        if 1 in d:
            while (d[1]):
                nums.append(1)
                d[1]-=1
        if 2 in d:
            while (d[2]):
                nums.append(2)
                d[2]-=1    
        