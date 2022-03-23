# Question: 12. Integer to Roman
# Link: https://leetcode.com/problems/integer-to-roman/
# Date: 21/3/2022
# Strategy:

class Solution:
    def intToRoman(self, num: int) -> str:
        value_to_symbol = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        numeral = ''
        for val in value_to_symbol.keys():
            if num // val > 0:
                numeral += value_to_symbol[val] * (num // val)
                num %= val
        return numeral


sol = Solution()
input = 3
print('Answer:', sol.intToRoman(input))
