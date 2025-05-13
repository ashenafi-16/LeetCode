# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        fir = []
        sec = []
        count = 0
        while x >  0:
            fir.append(x%2)
            x //= 2
        while y > 0:
            sec.append(y%2)
            y //= 2
        
        maxx = max(len(fir),len(sec))
        for i in range(maxx):
            a = fir[i] if i < len(fir) else 0
            b = sec[i] if i < len(sec) else 0
            if a != b:
                count += 1
        return count
        
