# Problem: Books - https://codeforces.com/contest/279/problem/B

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
    n,t = dif_num()
    num = numbers()
    total = 0
    left = 0
    maximum = float('-inf')
    for i in range(len(num)):
        total += num[i]
        while left < len(num) and total > t:
            total -= num[left]
            left += 1
        maximum = max(maximum,i-left + 1)
    print(maximum)
        

if __name__ == "__main__":
    solve()