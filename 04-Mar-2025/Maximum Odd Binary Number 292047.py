# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ['1']
        ones = s.count('1') - 1
        zeros = s.count('0')
        res.append('0'*zeros)
        res.append('1'* ones)
        return ''.join(res[::-1])
        