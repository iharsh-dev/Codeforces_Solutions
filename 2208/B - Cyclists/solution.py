t = int(input())
for _ in range(t):
    n, k, p, m = map(int, input().split())
    a = list(map(int, input().split()))
 
    win_cost = a[p - 1]
    others = a[:p-1] + a[p:]   
 
    first_cost = 0
    if p > k:
        before = sorted(a[:p-1])   
        first_cost = sum(before[:p-k])  
 
    between_cost = sum(sorted(others)[:n-k]) if n > k else 0
 
    cost = 0
    count = 0
 
    cost += first_cost + win_cost
    if cost <= m:
        count = 1
        while cost + between_cost + win_cost <= m:
            cost += between_cost + win_cost
            count += 1
 
    print(count)