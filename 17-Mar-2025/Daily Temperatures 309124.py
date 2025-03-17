# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = [0] * len(temperatures)
        for i in range(len(temperatures)):
            index[i] = i
        mapp = list(zip(temperatures,index))
        stk = []
        val = []
        for i in range(len(mapp)):
            while stk and mapp[i][0] > stk[-1][0]:
                temp = stk.pop()
                val.append((abs(mapp[i][1] - temp[1]),temp[1]))
            stk.append(mapp[i])
        sorted_val = sorted(val,key=lambda x:x[1])
        res = [0]* len(temperatures)
        for i in range(len(sorted_val)):
           
            res[sorted_val[i][1]] = sorted_val[i][0]

        return res
                
