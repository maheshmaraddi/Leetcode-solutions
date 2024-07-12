class Solution:
    def climbStairs(self, n: int) -> int:
        if n==2:return 2
        if n==1:return 1
        a=1
        b=2
        c=b
        for i in range(3,n+1):
            c=b+a
            a=b
            b=c
        return c


        