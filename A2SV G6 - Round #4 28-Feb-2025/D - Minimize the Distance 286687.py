# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
num = list(map(int,input().strip().split()))
def sol(num,n):
    num.sort()
    val = (n-1)//2
    return num[val]
        
    
print(sol(num,n))
