# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

import sys, math as m, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
number = lambda: int(sys.stdin.readline().strip())
dif_num = lambda: map(int, sys.stdin.readline().strip().split())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
def solve():
   n = number()
   pre_count = defaultdict(int)
   for _ in range(n):
       fir,sec = dif_num()
       pre_count[fir] += 1
       pre_count[sec+1] -= 1
   sorted_pre = sorted(pre_count.items(),key=lambda x:x[0])
   
   temp = 0
   arr = [0] * n
   for idx,val in sorted_pre:
       pre_count[idx] = temp + val
       temp += val
   ress = sorted(pre_count.items())
   itera = 0
   i = 0
   while i < len(ress) - 1:
        itera = i + 1
        # while itera < len(ress) and ress[i][1] == ress[itera][1]:
        #     itera += 1
        if ress[i][1]:
            arr[ress[i][1]-1] = (arr[ress[i][1]-1] + abs(ress[i][0] - ress[itera][0]))
        i = itera

   return arr
           
       
       

multi = False # if multiple Test cases change it to true
t = int(input()) if multi else 1
for _ in range(t):
    print(*solve())