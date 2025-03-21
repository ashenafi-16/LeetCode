# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

n = int(input())
num = list(map(int, input().strip().split()))
x = int(input())
val = list(map(int, input().strip().split()))
def solutions(n,num,x,val):
    if sum(val) != sum(num):
        return -1
    else:
        one = []
        two = []
        l = 0
        r = 0 
        first = 0
        second = 0
        first += num[l]
        second += val[r]
        while l < n and r < x:
                
            if first == second:

                one.append(first)
                two.append(second)
                l += 1
                r += 1
                if l < n and r < x:
                    first += num[l]
                    second += val[r]
            elif first < second:
                l += 1
                first += num[l]
            else:
                r += 1
                if r < x:
                    second += val[r]
        return len(one)

print(solutions(n,num,x,val))
