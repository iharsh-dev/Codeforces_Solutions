t = int(input())
ans = []
for _ in range(t):
    n, qu = map(int,input().split())
    a = list(map(int,input().split()))
    q = list(map(int,input().split()))
    c = q[:]
    c.sort()
    height=[0]*(n+1)
    for i in range(n):
        height[i+1] = height[i] + a[i]
    j=0
    arr = []
    mapa = {}
    for i in range(qu):
        while j < n and c[i]>=a[j]:
            j+=1
        mapa[c[i]]=height[j]
    for i in q:
        arr.append(mapa[i])
    ans.append(arr)
for i in ans:
    print(*i)