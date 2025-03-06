# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

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
    for _ in range(n):
        x = number()
        num = numbers()
        l = 0
        r = 1
        count =0
        while l < x and r < x:
            if num[l] > num[r]:
                count += 1
                l += 2
                r += 2
            else:
                l += 1
                r += 1
        print(count)

if __name__ == "__main__":
    solve()