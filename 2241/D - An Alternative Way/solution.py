t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    start = 0
    check = True
    for i in range(n):
        start+=(b[i] - a[i])
        if start < 0:
            check = False
    if check:
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)