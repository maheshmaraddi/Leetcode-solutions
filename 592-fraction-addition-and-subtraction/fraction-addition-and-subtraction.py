import re
from fractions import Fraction
from typing import List
class Solution:
    def fractionAddition(self, expression: str) -> str:
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        # Initialize the result as a Fraction object
        result = Fraction(0, 1)

        # Iterate over each fraction in the expression
        for frac in fractions:
            result += Fraction(frac)

        # Convert the result to an irreducible fraction
        result = result.limit_denominator()

        # Format the result as required
        return f"{result.numerator}/{result.denominator}"