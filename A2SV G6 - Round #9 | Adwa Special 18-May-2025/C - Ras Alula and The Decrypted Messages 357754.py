# Problem: C - Ras Alula and The Decrypted Messages - https://codeforces.com/gym/601269/problem/C

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
    s,w = dif_num()
    dec = list(word())
    inc = list(word())
    for i in range(len(dec)):
        dec[i] = ord(dec[i])
    total = 0
    for val in inc:
        total += ord(val)
    t = len(inc)
    ini = sum(dec[:t-1])
    left = 0
    for i in range(t-1,len(dec)):
        ini += dec[i]
        if ini == total:
            return "YES"
        ini -= dec[left]
        left += 1


    return 'NO'
        
        

if __name__ == "__main__":
    n = number()
    for _ in range(n):
        print(solve())