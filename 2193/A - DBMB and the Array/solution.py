t=int(input())
ans=[]
for i in range(t):
    n,s,x=map(int,input().split())
    a=list(map(int,input().split()))
    if (s-sum(a))%x==0 and s-sum(a)>=0:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)