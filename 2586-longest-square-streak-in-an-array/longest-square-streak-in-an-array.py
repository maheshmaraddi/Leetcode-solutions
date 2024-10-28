class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        res=-1
        d={}
        nums=set(nums)
        for i in nums:
            d[i] =1
        for x in nums:
            if x**2  in nums:
                i=x
                c=1
                while(i**2 in nums):
                    c+=1
                    i=i**2
                    # i+=1
                res=max(res,c)
                if res==5:break
        return res