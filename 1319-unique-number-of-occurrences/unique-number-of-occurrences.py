class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=[]
        for i in d:
            l.append(d[i])
        print(len(set(l)))
        return len(l)==len(set(l))

        