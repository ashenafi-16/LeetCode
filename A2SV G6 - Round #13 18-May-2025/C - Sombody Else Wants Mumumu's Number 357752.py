# Problem: C - Sombody Else Wants Mumumu's Number - https://codeforces.com/gym/607625/problem/C

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
    nums = numbers()
    count = defaultdict(int)
    for i in range(len(nums)):
        count[nums[i]] -= 1
    temp = list(count.values())
    heap.heapify(temp)
    nn = 0
    while temp:
        
        node = heap.heappop(temp)
        if temp:
            nn = heap.heappop(temp)
        else:
            heap.heappush(temp,node)
            break
        
        
        
        if node + 1 <0:
            heap.heappush(temp,node+1)
        if nn + 1 <0:
            heap.heappush(temp,nn + 1)
    return abs(sum(temp))


            

if __name__ == "__main__":
    n = number()
    for _ in range(n):
        print(solve())