t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    c = a[0]
    for i in range(1,n):
        c = a[i]&c 
    ans.append(c)
for i in ans:
    print(i)