class Solution:
    def pow_mod(self,a, b):
        result = 1
        for _ in range(b):
            result = (result * a) % 1337
        return result

    def superPow(self,a: int, b: List[int]) -> int:
        result = 1
        for digit in b:
            result = self.pow_mod(result, 10) * self.pow_mod(a, digit) % 1337
        return result
        