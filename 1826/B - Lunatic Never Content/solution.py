import math
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    j = n-1 
    if i < j:
        g1 = abs(a[i]-a[j])
        while i < j:
            g1 = math.gcd(g1,abs(a[i]-a[j]))
            i+=1
            j-=1
        ans.append(g1)
    else:
        ans.append(0)
for i in ans:
    print(i)