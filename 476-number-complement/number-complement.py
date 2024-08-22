class Solution:
    def findComplement(self, num: int) -> int:
        n=num
        c=0
        while n:
            n=n>>1
            c+=1
        mask = 2**c -1
        # print(mask)
        return mask^num