# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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
    n,k = dif_num()
    num = numbers()
    stk = deque()
    count = 0
    l = 0
    minimum = float('inf')
    maximum = float('-inf')
    for i in range(n):
        
        if num[i] < minimum:
            minimum = num[i]
        if num[i] > maximum:
            maximum = num[i]
        if (maximum - minimum) > k:
            minimum = float('inf')
            maximum = float('-inf')
            if num[i] < minimum:
                minimum = num[i]
            if num[i] > maximum:
                maximum = num[i]
            l = len(stk) - 1       
            while l >= 0 and abs(num[i] - stk[l]) <= k:     
                if stk[l] < minimum:
                    minimum = stk[l]
                if stk[l] > maximum:
                    maximum = stk[l]
                l -= 1
            while l >= 0:
                stk.popleft()
                l -= 1
            
            
        stk.append(num[i])
        count += len(stk)
        temp = i
    # if l != temp:
    #     count += ((abs(temp-l + 1)*abs(temp-l+2))//2)

           

    print(count)




if __name__ == "__main__":
    solve()