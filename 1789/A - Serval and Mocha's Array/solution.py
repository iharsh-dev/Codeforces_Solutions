import math
 
t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    a.sort()
    check=0
    gcd=a[0]
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(a[i],a[j])<3:
                check=1
                break
    if check:
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)