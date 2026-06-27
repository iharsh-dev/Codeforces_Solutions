t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] != 1:
        ans.append('NO')
    else:
        mapa = [0]*(n+1) 
        for i in range(n):
            mapa[i+1] = mapa[i] + a[i]
        check = 1
        for i in range(1,n):
            if a[i] > mapa[i]:
                check = 0
                break
        if check:
            ans.append('YES')
        else:
            ans.append('NO')
for i in ans:
    print(i)