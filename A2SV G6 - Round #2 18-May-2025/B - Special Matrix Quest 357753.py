# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

row = int(input())
matrix = []
from collections import defaultdict
for _ in range(row):
    matrix.append([int(i) for i in input().split()])
index_store = defaultdict(int)
total = 0
k = 0
flag = False
i = k
j = 0
while i < len(matrix) and j < len(matrix):
    index_store[(i,j)] += 1
    i += 1
    j += 1
    
i = len(matrix)-1
j = k
while i >= 0 and j < len(matrix):
    index_store[(i,j)] += 1
    i -= 1
    j += 1
row = 0 
col = 0
j = len(matrix)//2
while row < len(matrix) :
    index_store[(row,j)] += 1
    index_store[(j,col)] += 1
    row += 1
    col += 1
for index in index_store.keys():
    total += matrix[index[0]][index[1]]
print(total)