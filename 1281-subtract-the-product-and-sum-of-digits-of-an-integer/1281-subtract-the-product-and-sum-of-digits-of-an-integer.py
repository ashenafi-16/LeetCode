class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        pro = 1
        while n != 0:
            sum += n %10
            pro *= n%10
            n//=10
        return pro - sum
