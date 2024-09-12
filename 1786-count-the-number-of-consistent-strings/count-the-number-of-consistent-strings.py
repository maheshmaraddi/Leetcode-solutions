class Solution:
    def countConsistentStrings(self, a: str, w: List[str]) -> int:
        a = set(a)
        count = 0
        
        for word in w:
            for letter in word:
                if letter not in a:
                    count += 1
                    break
        
        return len(w) - count