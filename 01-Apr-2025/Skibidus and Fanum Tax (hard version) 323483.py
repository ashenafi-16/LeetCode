# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

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
    n,m = dif_num()
    input = numbers()
    arr = [float('-inf')]
    val = numbers()
    val.sort()
    arr.extend(input)
    for i in range(1,len(arr)):
        low = 0
        high = len(val) - 1
        ini = arr[i] if arr[i] >= arr[i-1] else float('inf')
        while low <= high:
            mid = (low + high) // 2
            if (val[mid] - arr[i]) >= arr[i-1]:
                high = mid - 1
                ini = min(ini,(val[mid] - arr[i]))
            else:
                low = mid + 1
       
        arr[i] = ini
        if arr[i] < arr[i-1] or ini == float('inf'):
            return "NO"
    return "YES"
if __name__ == "__main__":
    n = number()
    for _ in range(n):

        print(solve())