# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
    n,x = dif_num()
    nums = []
    for _ in range(x):
        temp = numbers()
        nums.append(temp[::-1])
    nums.sort()
    graph = {i:i for i in range(1,n+1)}
    size = [1] * (len(graph) + 1)
    def find(x):
        while x != graph[x]:
            graph[x] = graph[graph[x]]
            x = graph[x] 
        return graph[x]
    def union(x,y):
        root1 = find(x)
        root2 = find(y)
        if root1 == root2:
            return False
        else:
            if size[root1] > size[root2]:
                graph[root1] = graph[root2]
                size[root1] += size[root2]
            else:
                graph[root2] = graph[root1]
                size[root2] += size[root1]
        return True
    res = 0
    for wei,fir,sec in nums:
        if union(fir,sec):
            res += wei
    return res
        
    

if __name__ == "__main__":
    print(solve())