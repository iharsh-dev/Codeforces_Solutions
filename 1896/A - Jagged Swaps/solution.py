t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if a[0]==1:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)