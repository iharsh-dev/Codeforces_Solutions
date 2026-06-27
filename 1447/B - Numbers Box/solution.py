t = int(input())
ans = []
for _ in range(t):
    n, m = map(int,input().split())
    grid = []
    for i in range(n):
        a = list(map(int,input().split()))
        grid.append(a)
    count = 0
    for i in range(n):
            count += sum(1 for x in grid[i] if x < 0)
    for i in range(n):
        for j in range(m):
            if grid[i][j] < 0:
                grid[i][j]*=(-1)
    some = 0
    for i in grid:
            some+=sum(i)
    check=0
    if any(0 in row for row in grid):
        check=1
    if check:
        ans.append(some)
    else:
        if count%2==0:
            ans.append(some)
        else:
            minn=min(grid[0])
            for i in range(1,n):
                x = min(grid[i])
                if x < minn:
                    minn=x 
            ans .append(some-2*minn)
for i in ans:
    print(i)