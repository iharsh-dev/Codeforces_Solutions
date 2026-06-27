t=int(input())
ans=[]
for i in range(t):
    n,k=map(int,input().split())
    if n%2==0:
        ans.append("YES")
    elif n%2!=0 and k%2!=0:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)