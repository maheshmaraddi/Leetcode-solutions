class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c=0
        n=len(arr)
        if n==2:return 1
        fr=0
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        sum = 0
        val = sorted(d.values(),reverse=True)
        for v in val:
            sum+=v
            c+=1
            if sum>=n//2:break
        return c