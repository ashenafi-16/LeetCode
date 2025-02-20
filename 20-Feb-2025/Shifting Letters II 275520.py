# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        char_list = [0]*(len(s)+1)
        for i in range(len(s)):
            char_list[i] = ord(s[i])
        print(char_list)
        pre_sum = [0]*(len(s)+1)
        for i,j,k in shifts:
            if k == 0:
                pre_sum[i] =  pre_sum[i] - 1
                pre_sum[j+1] = (pre_sum[j+1] + 1)
            else:
                pre_sum[i] =  pre_sum[i] + 1
                pre_sum[j+1] = (pre_sum[j+1] - 1)
        for i in range(1,len(pre_sum)):
            pre_sum[i] = pre_sum[i] + pre_sum[i-1]
        for i in range(len(char_list)):
            char_list[i] = (pre_sum[i] + char_list[i])
        for i in range(len(char_list)):
            char_num = (char_list[i]-ord('a'))% 26
            char_num += ord('a')
            char_list[i] = char_num
        for i in range(len(char_list)):
            char_list[i] = chr(char_list[i])
        return "".join(char_list[:-1])
            