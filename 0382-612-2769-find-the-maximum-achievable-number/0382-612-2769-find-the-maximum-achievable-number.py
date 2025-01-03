class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        while t != 0:
            num += 2
            t -= 1
        return num