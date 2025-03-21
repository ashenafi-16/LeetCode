# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

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
    x = number()
    st = word()
    count = defaultdict(int)
    temp = defaultdict(int)
    for val in st:
        count[val] += 1
    maximum = len(count)
    for val in st:
        temp[val] += 1
        count[val] -= 1
        if count[val] <= 0:
            del count[val]
        if maximum < len(temp) + len(count):
            maximum = len(temp)+len(count)
    return maximum

if __name__ == "__main__":
    n = number()
    for _ in range(n):
        print(solve())