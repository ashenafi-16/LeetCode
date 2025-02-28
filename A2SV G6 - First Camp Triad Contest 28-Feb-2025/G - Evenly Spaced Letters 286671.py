# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

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
   strings = list(word())
   strings.sort()
   return ''.join(strings)
multi = True # if multiple Test cases change it to true
t = int(input()) if multi else 1
for _ in range(t):
    print(solve())