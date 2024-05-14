class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=0
        n=len(arr)
        d={}
        for i in arr:
            d[i] = 1 + d.get(i,0)
        sum = 0
        val = sorted(d.values(),reverse=True)
        for v in val:
            sum+=v
            c+=1
            if sum>=n//2:break
        return c