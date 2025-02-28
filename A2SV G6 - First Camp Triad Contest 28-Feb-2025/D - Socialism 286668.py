# Problem: D - Socialism - https://codeforces.com/gym/589822/problem/D

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
    n,x = dif_num()
    num = numbers()
    num.sort(reverse=True)
    diff_value = 0
    count = 0
    for i in range(len(num)):
        if num[i] >= x:
            diff_value += (num[i] - x)
            count += 1
        else:
            if num[i] + diff_value >= x:
                diff_value -= (x - num[i])
                count += 1
    return count
  
multi = True # if multiple Test cases change it to true
t = int(input()) if multi else 1
for _ in range(t):
    print(solve())