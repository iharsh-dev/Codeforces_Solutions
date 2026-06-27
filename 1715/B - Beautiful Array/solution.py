t = int(input())
ans = []
for _ in range(t):
    n, k, b, s = map(int,input().split())
    arr = []
    if k*b <= s <= (k*b + (k-1)*n) :
        if s >= k*b+k-1:
            arr.append(k*b + k - 1)
            s-=(k*b+k-1)
        else:
            arr.append(s)
            s = 0
        for i in range(n-1):
            if s >= k-1:
                arr.append(k-1)
                s -= (k-1)
            else:
                arr.append(s)
                s-=s
    else:
        arr.append(-1)
    ans.append(arr)
for i in ans:
    print(*i)