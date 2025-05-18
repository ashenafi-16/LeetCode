# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        arr = set()
        n = len(s)
        
        for i in range(1<<n):
            temp = list(s)
            for j in range(n):
                if i & (1 << j):
                    if temp[j].isalpha():
                        temp[j] = temp[j].lower() if temp[j].isupper() else temp[j].upper()
                        
            arr.add(''.join(temp))
        return list(arr)
