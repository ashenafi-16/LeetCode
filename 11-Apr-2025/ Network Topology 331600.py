# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

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
    node,edge = dif_num()
    incoming = defaultdict(int)
    
    for i in range(edge):
        f,s = dif_num()
        incoming[f] += 1
        incoming[s] += 1
    
    res = max(incoming.values())
    if node == edge and res <= 2:
        return "ring topology"
    if res == node - 1 and res == edge:
        return "star topology"
    
    for fir ,se in incoming.items():
        if se> 2:
            return "unknown topology"
    return "bus topology"

   
    

if __name__ == "__main__":
    print(solve())