t = int(input())
ans = []
for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    cons = []
    i = 0
    while i < n:
        temp = a[i]
        count = 0
        while i < n and a[i]==temp:
            count+=1
            i+=1
        cons.append(count)
    cons.sort(reverse=True)
    if cons[0] <= m-1:
        ans.append('YES')
    else:
        ans.append('NO')
for i in ans:
    print(i)