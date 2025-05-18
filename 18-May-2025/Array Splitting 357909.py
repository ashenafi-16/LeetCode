# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

import sys, random, cmath,math
from collections import defaultdict, Counter
from math import inf

xors = random.randint(1, 1_000_000_000)
def con(x): return x ^ xors
def sp_num(): return map(int,sys.stdin.readline().split())
def number(): return int(sys.stdin.readline().strip())
def numbers(): return list(map(int, sys.stdin.readline().strip().split()))
def word(): return sys.stdin.readline().strip()
def words(): return sys.stdin.readline().strip().split()
def char(): return sys.stdin.read(1)
def chars(): return list(sys.stdin.readline().strip())
def matrix(n): return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
def str_matrix(n): return [sys.stdin.readline().strip() for _ in range(n)]
def yn(cond): return 'YES' if cond else 'NO'

def solve():
    x,k = sp_num()
    num = numbers()
    if x == k:
        return 0
    maxN = max(num)
    minN = min(num)
    res = maxN - minN
    arr = []
    for i in range(1,len(num)):
        arr.append(num[i] - num[i-1])
    arr.sort(reverse= True)
    temp = 0
    for i in range(k-1):
        temp += arr[i]

    return res - temp

if __name__ == "__main__":
    print(solve())