# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys, math as m, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint

number = lambda: int(sys.stdin.readline().strip())
dif_num = lambda: map(int, sys.stdin.readline().strip().split())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split(' ')
word = lambda: sys.stdin.readline().strip()
yn = lambda condition: 'YES' if condition else 'NO'

test = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand

def solve():
    n,que = dif_num()
    graph = {i:i for i in range(1,n+1)}
    graph[-1] = -1
    def find(x):
        while x != graph[x]:
            graph[x] = graph[graph[x]]
            x = graph[x] 
        return graph[x]
    def union(x,y):
        
        root1 = find(x)
        root2 = find(y)
        graph[root1] = root2
    for _ in range(que):
        val = words()
        
        if val[0] == '-':
            if int(val[1]) == n:
                union(int(val[1]),-1)
            else:
                union(int(val[1]),(int(val[1]) + 1))
        elif val[0] == '?':
            print(find(int(val[1])))
        


if __name__ == "__main__":
    solve()