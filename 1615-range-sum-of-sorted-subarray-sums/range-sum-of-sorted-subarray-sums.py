class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        mod = 10**9 +7
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                l.append(s)
        l.sort()
        return sum(l[left-1:right])%mod