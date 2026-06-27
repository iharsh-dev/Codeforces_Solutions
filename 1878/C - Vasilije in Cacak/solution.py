t = int(input())
ans=[]
for _ in range(t):
    n, k, x = map(int,input().split())
    som1 = ((n-k+1)*(n-k))//2
    som2 = (n*(n+1))//2-som1
    som3 = (k*(k+1))//2
    if x>som2:
        ans.append('NO')
    elif x<som3:
        ans.append('NO')
    else:
        ans.append('YES')
for i in ans:
    print(i)