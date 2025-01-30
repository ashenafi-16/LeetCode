class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        array = []
        if num % 3 != 0:
            return []
        else:
            num = num // 3
            return [num-1,num,num+1]
        
