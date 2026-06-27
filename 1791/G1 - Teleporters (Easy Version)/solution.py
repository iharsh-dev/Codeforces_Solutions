t = int(input())
ans = []
for _ in range(t):
    n, c = map(int,input().split())
    a = list(map(int,input().split()))
    coins = []
    for i in range(n):
        coins.append((i+1)+a[i])
    coins.sort()
    summ = 0
    count = 0
    for i in range(n):
        if summ + coins[i] <= c:
            summ += coins[i]
            count += 1
        else:
            break
    ans.append(count)
for i in ans:
    print(i)