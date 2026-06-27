t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n!=1:
        k = []
        for i in range(1,n):
            if n % i == 0 :
                k.append(i)
        arr = []
        for i in k:
            som = []
            for j in range(0,n,i):
                som.append(sum(a[j:j+i]))
            arr.append(max(som)-min(som))
        ans.append(max(arr))
    else:
        ans.append(0)
for i in ans:
    print(i)