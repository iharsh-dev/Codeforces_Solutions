import math
t = int(input())
ans=[]
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    arr = 0
    for j in range(1,n-1):
        g = math.gcd(a[j], a[j+1])
        c = math.gcd(a[j-1], a[j])
        check = (g*c)//math.gcd(g, c)
        if a[j]>check:
            arr += 1
    g = math.gcd(a[0], a[1])
    c = math.gcd(a[n-1],a[n-2])
    if a[0]>g:
        arr += 1
    if a[n-1]>c:
        arr += 1
    ans.append(arr)
for i in ans:
    print(i)