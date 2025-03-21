# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

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
    row,col = dif_num()
    matrix = []
    for i in range(row):
        temp = word()
        matrix.append(list(temp))
    for i in range(row):
        for j in range(col):
            temp = matrix[i][j]
            
            if temp == '*':
                continue
            else:
                count = 0
                for t in range(i - 1,i + 2):
                    if t < 0:
                        continue
                    for m in range(j-1,j+2):
                        
                        if m < 0:
                            continue
                        if  t < row and (m >= 0 and m < col):
                            if i == t and j ==m:
                                continue
                            
                            if matrix[t][m] == '*':
                                count += 1
                
                if matrix[i][j] == '.':
                    if count > 0:
                        return "NO"
                if matrix[i][j].isdigit():
                    if int(matrix[i][j]) != count:
                        return "NO"
    return "YES"



if __name__ == "__main__":
    
    print(solve())