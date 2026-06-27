t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans.append(a)
for i in ans:
    print(*i)