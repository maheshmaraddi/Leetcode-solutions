class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d={}
        for i in arr:
            d[i]= 1+ d.get(i,0)
        c=0
        for i in d:
            if d[i]==1:
                c+=1
                if c==k:
                    return i
        return ''