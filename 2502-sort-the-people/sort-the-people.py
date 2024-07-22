class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a= list(zip(names,heights))
        aa=sorted(a,key= lambda x:x[1],reverse=True)
        return [i[0] for i in aa]
        