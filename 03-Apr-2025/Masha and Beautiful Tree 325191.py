# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

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
    value = numbers()
    count = 0
    def mergesort(left_arr,right_arr):
        nonlocal count 
        merged = []
        left_sum = sum(left_arr)
        right_sum = sum(right_arr)
        if left_sum > right_sum:
            merged.extend(right_arr)
            merged.extend(left_arr)
            count += 1
        else:
            merged.extend(left_arr)
            merged.extend(right_arr)
        return merged

    def sorting(left,right,value):
        if left >= right:
            return [value[left]]
        mid = (left + right) // 2

        left_arr = sorting(left,mid,value)
        right_arr = sorting(mid+1,right,value)
        
        return mergesort(left_arr,right_arr)
    
    val = (sorting(0,x-1,value))
    for i in range(1,len(val)):
        if val[i] < val[i-1]:
            return -1
    return count


if __name__ == "__main__":
    n = number()
    for _ in range(n):
        print(solve())