t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=[ i for i in range(1,n+1)]
    a.reverse()
    ans.append(a)
for i in ans:
    print(*i)