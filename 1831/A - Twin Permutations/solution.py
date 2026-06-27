t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    maxx=n+1
    b=[]
    for i in a:
        b.append(maxx-i)
    ans.append(b)
for i in ans:
    print(*i)