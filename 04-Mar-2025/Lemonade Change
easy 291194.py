# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_five = 0
        count_ten = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                count_five += 1
            if bills[i] == 10:
                if count_five > 0:
                    count_five -= 1
                else:
                    return False
                count_ten += 1
            if bills[i] == 20:
                if count_ten > 0 and count_five > 0:
                    count_ten -= 1
                    count_five -= 1
                elif count_five >=3 :
                    count_five -= 3
                else:
                    return False
        return True
            
            
