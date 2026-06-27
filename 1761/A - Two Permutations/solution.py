t=int(input())
ans=[]
for _ in range(t):
    n, a, b = map(int,input().split())
    if a==b==n:
        ans.append('YES')
    elif a+b>=n or a+b==n-1:
        ans.append('NO')
    else:
        ans.append('YES')
for i in ans:
    print(i)