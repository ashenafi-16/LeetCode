# Problem: C - Chain Reaction in the Math Club - https://codeforces.com/gym/606404/problem/C

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
    n,x = sp_num()
    graph = defaultdict(list)
    count = defaultdict(int)
    for _ in range(x):
        a,b = sp_num()
        graph[a].append(b)
        graph[b].append(a)
        count[a] += 1
        count[b] += 1
    res = 0
    def func(idx):
        count[idx] -= 1
        
        for neigh in graph[idx]:
            count[neigh] -= 1
    cond = True
    while cond:
        cond = False
        arr = []
        for idx ,val in count.items():
            if val == 1:
                cond = True
                arr.append(idx)
        
                
        if cond:
            for i in range(len(arr)):
                func(arr[i])
            res += 1
    return res 
                   

if __name__ == "__main__":
    print(solve())