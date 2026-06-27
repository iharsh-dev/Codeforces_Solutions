t=int(input())
ans=[]
for _ in range(t):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    mapp=[0]*(n+1)
    for i in range(n):
        mapp[i+1]=(mapp[i]+a[i])%2
    b=mapp[n]
    for i in range(q):
        l,r,k=map(int,input().split())
        leng=(r-l+1)%2
        sub=(mapp[r]-mapp[l-1])%2
        new=(b-sub+(k%2)*leng)%2
        if new:
            ans.append('YES')
        else:
            ans.append('NO')
for i in ans:
    print(i)