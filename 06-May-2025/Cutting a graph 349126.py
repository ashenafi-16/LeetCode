# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
    ver,edg,op = dif_num()
    graph = {i:i for i in range(1,ver+1)}
    arr = []
    res = []
    def find(x):
        while x != graph[x]:
            graph[x] = graph[graph[x]]
            x = graph[x]
        return graph[x]
    def union(x,y):
        root1 = find(x)
        root2 = find(y)
        graph[root1] = graph[root2]
    for _ in range(edg):
        a,b = dif_num()
    for _ in range(op):
        num = words()
        arr.append([int(num[1]),int(num[2]),num[0]])
    for i in range(len(arr)-1,-1,-1):
        if arr[i][2] == 'cut':
            union(arr[i][0],arr[i][1])
        elif arr[i][2] == 'ask':
            res.append(yn(find(arr[i][0]) == find(arr[i][1])))
    for i in range(len(res)-1,-1,-1):
        print(res[i])
                 

if __name__ == "__main__":
    solve()