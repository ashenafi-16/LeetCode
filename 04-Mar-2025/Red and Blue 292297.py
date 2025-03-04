# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

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
        num1 = numbers()
        y  = number()
        num2 = numbers()
        maxx1 = float('-inf')
        maxx2 = float('-inf')
        sum1 = 0
        sum2 = 0
        for i in range(x):
            sum1 += num1[i]
            if sum1 > maxx1:
                maxx1 = sum1
        for i in range(y):
            sum2 += num2[i]
            if sum2 > maxx2:
                maxx2 = sum2
        fir = max(0,maxx1)
        res  = max(fir+0 , maxx2+fir)
        print(res)        

if __name__ == "__main__":
    solve()