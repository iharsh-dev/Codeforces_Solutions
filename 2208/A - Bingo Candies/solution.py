t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=[]
    for i in range(n):
        b=list(map(int,input().split()))
        b.sort()
        a.append(b)
    c=[]
    for i in range(n):
        c.append(max(a[i]))
    colors=[0]*(max(c)+1)
    for i in range(n):
        for j in range(n):
            colors[a[i][j]]+=1 
    c=n**2-n
    check=0
    for i in colors:
        if i>c:
            check=1
    if check==1:
        ans.append('NO')
    else:
        ans.append('YES')
for i in ans:
    print(i)