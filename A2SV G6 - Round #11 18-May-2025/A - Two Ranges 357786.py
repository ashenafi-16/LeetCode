# Problem: A - Two Ranges - https://codeforces.com/gym/604781/problem/A

import sys, random, cmath
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
    a,b,c,d = sp_num()
    ans = [a]
    if c == a:
        ans.append(d)
    else:
        ans.append(c)
    print(*ans)

    


if __name__ == "__main__":
    n = number()
    for _ in range(n):
        (solve())