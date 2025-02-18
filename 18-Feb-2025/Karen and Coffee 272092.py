# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n , k , q = map(int, input().split())
counter = [0] * 200002

for i in range(n):
    start, end = map(int, input().split())
    counter[start] += 1
    counter[end + 1] -= 1

for i in range(1,len(counter)):
    counter[i] += counter[i-1]
for i in range(len(counter)):
    if counter[i] < k:
        counter[i] = 0
    else:
        counter[i] = 1
for i in range(1,len(counter)):
    counter[i] = counter[i] + counter[i-1]
for _ in range(q):
    start, end = map(int, input().split())
    print(counter[end] - counter[start-1])


