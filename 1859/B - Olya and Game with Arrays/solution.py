t = int(input())
ans = [] 
for _ in range(t) :
    n = int(input())
    arr = []
    for i in range(n) : 
        a = int(input())
        b = list(map(int,input().split()))
        b.sort()
        arr.append(b) 
    arr.sort()
    brr = []
    for i in range(len(arr)):
        brr.append(arr[i][1])
    c = brr.index(min(brr))
    som = sum(brr) - brr[c] + arr[0][0] 
    ans.append(som) 
for i in ans : 
    print(i)