t = int(input())
 
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    target = a[-1]
    length = 1
    ans = 0
 
    while length < n:
        if a[n - length - 1] == target:
            length += 1
        else:
            ans += 1
            length *= 2
 
    print(ans)