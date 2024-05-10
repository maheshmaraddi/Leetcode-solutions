class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        d={}
        nums.sort()
        while nums:
            a = nums.pop(0)
            b = nums.pop()
            c = (a+b)/2
            d[c] = 1 + d.get(c,0)
        print(d)
        return len(d)