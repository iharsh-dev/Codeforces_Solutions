import math
cop = []
for i in range(1,1001):
    for j in range(1,1001):
        if math.gcd(i,j) == 1:
            cop.append((i,j))
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = set(a)
    maxx = -1
    arr = [-1]*1001
    for i in range(n):
        arr[a[i]] = (i+1)
    for x,y in cop:
        if arr[x] != -1 and arr[y] != -1:
            maxx = max(maxx,arr[x]+arr[y])
    ans.append(maxx)
for i in ans:
    print(i)
    