# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

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
    num = numbers()
    sorted_val = sorted(num)
    for i in range(1,n):
        num[i] = num[i] + num[i-1]
        sorted_val[i] = sorted_val[i] + sorted_val[i-1]

    num_question = number()
    for _ in range(num_question):
        type,l , r = dif_num()
        if type == 1:
            res = num[r-1] - num[l-2] if l-2>= 0 else num[r-1]
        else:
            res = sorted_val[r-1] - sorted_val[l-2] if l-2>= 0 else sorted_val[r-1]
        print(res)

if __name__ == "__main__":
    solve()