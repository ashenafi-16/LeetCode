# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        t = (2**n) - 1

        def kthfind(t,k):
            if t == 1:
                return '0'
            mid = t//2
            if k <= mid:
                return kthfind(mid,k)
            elif k > mid + 1:
                res = kthfind(mid, 1+ t - k)
                return '0' if res == '1' else '1'
            else:
                return '1'
          
        return kthfind(t,k)
