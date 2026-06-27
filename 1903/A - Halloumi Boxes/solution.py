t=int(input())
ans=[]
for i in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    c=x[:]
    c.sort()
    if c==x:
        ans.append("YES")
    elif k<2:
        ans.append("NO")
    else:
        ans.append("YES")
for i in ans:
    print(i)