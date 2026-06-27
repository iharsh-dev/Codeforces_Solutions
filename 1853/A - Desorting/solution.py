t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=a[:]
    b.sort()
    if a==b:
        minn=max(a)
        for i in range(n-1):
            diff = a[i+1]-a[i]
            if diff<minn:
                minn=diff
        ans.append(minn//2+1)
    else:
        ans.append(0)
for i in ans:
    print(i)
        