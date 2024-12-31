class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            r = i + 1
            pre_sum = 0
            while r < len(arr):
                pre_sum += arr[r]
                if (r - i + 1) % 2 != 0:
                    total += (pre_sum + arr[i])
                r += 1
        return total