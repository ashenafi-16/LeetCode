# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res = [arr] * (len(arr))
        temp  = 0
        ans = []
        for i in range(len(arr)):
            temp ^= arr[i]
            res[i] = temp
        for fir,sec in queries:
            t = res[fir-1] if fir - 1 >= 0 else 0
            ans.append(t ^ res[sec])
        return ans



        