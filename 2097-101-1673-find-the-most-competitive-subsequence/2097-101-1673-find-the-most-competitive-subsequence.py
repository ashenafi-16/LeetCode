class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and len(stack) + (n - i) > k:
                stack.pop()
            if len(stack) < k:
                stack.append(num)
        
        return stack