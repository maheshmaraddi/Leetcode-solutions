class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s=0
        cz= 0 
        ans = 0
        e= 0
        while e<len(nums):
            
            if nums[e] ==0:
                cz+=1
            while cz>k:
                if nums[s]==0:
                    cz-=1
                s+=1
            ans= max(e-s+1,ans)
            e+=1
        return ans

        