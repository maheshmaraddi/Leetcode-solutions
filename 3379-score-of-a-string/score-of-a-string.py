class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        i=1
        while i<len(s):
            x= abs(ord(s[i])-ord(s[i-1]))
            ans+=x
            i+=1
        return ans
        