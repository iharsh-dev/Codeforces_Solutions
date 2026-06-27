t = int(input())
ans = []
for _ in range(t):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    pref = [0]*(n+1)
    for i in range(n):
        pref[i+1] = pref[i] + a[i]
    sugar = 0
    prev = 0
    for i in range(n,0,-1):
        count = 0
        if pref[i] <= x :
            count = 1 + (x-pref[i])//i - prev
            prev+=count 
            sugar += count*i 
    ans.append(sugar)
for i in ans:
    print(i)