t = int(input())
ans = []
for _ in range(t):
    x, y =map(int,input().split())
    if x % y == 0:
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)