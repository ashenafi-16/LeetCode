# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

import sys, math as m, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint
number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'
test = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
def solve():
   input = numbers()
   n = input[0]
   m = input[1]
   lis_num = [0]*n
   for i in range(n):
       lis_num[i] = numbers()
   dura = numbers()
   
   pre_sum = [0] * (m)
   start = 0
   res = 0
   for idx,val in lis_num:
       
       while start < len(dura) and res >= dura[start]:
          start += 1
       if start < len(dura):
        pre_sum[start] = pre_sum[start] + 1
       res += idx * val
   for i in range(1,len(pre_sum)):
       pre_sum[i] = pre_sum[i-1] + pre_sum[i]
   
   return pre_sum

multi = False # if multiple Test cases change it to true
t = int(input()) if multi else 1
for _ in range(t):
    res = solve()
    for i in res:
        print(i)