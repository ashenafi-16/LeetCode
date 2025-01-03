class Solution:
    def countDigits(self, num: int) -> int:
        div = str(num)
        count = 0
        for i in range(len(div)):
            if num % int(div[i]) == 0:
                count += 1
        return count