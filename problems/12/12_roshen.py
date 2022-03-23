# Question: 12. Integer to Roman
# Link: https://leetcode.com/problems/integer-to-roman/
# Date: 21/3/2022
# Strategy:

class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_symbol = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        numeral = ''
        for val in reversed(sorted(value_to_symbol.keys())):
            if num // val > 0:
                numeral += value_to_symbol[val] * (num // val)
                num %= val
        return numeral


sol = Solution()
input = 1994
print('Answer:', sol.intToRoman(input))
