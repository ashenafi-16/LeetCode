class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right +1):
            check = True
            nums = i
            while nums != 0: 
                if nums%10 == 0:
                    check=False
                elif i % (nums%10) != 0:
                    check = False
                nums//=10
            if check == True:
                result.append(i)
        return result
            