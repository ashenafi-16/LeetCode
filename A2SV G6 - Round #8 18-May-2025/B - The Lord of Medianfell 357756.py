# Problem: B - The Lord of Medianfell - https://codeforces.com/gym/599383/problem/B

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
    a,b =  sp_num()

    if a & 1:
        a = math.ceil(a/2)
    else:
        a = (a // 2) + 1
    return b //a

    

if __name__ == "__main__":
    n = number()
    for _ in range(n):

        print(solve())