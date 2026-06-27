t =int(input())
ans = []
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a = input()
        b = [int(x) for x in a]
        arr.append(b)
    count = 0
    for j in range(n//2):
        for i in range(j,n-1-j):
            some = arr[j][i] + arr[i][n-1-j] + arr[n-1-j][n-1-i] + arr[n-1-i][j]
            count += min(some ,4 - some)
    ans.append(count)
for i in ans:
    print(i)