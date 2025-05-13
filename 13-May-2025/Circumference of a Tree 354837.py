# Problem: Circumference of a Tree - https://codeforces.com/gym/102694/problem/A

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
    graph = defaultdict(list)
    if n == 1:
        return 0
    for _ in range(n-1):
        a,b = dif_num()
        graph[a].append(b)
        graph[b].append(a)
    def bfs(start):
        visited = {start: 0}
        queue = deque([start])
        farthest_node = start
        max_dist = 0
        
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited[neighbor] = visited[node] + 1
                    queue.append(neighbor)
                    if visited[neighbor] > max_dist:
                        max_dist = visited[neighbor]
                        farthest_node = neighbor
        return farthest_node,max_dist
    f_node,max_di = bfs(1)
    f_n,diameter = bfs(f_node)
    return diameter*3

    

  
if __name__ == "__main__":
    print(solve())