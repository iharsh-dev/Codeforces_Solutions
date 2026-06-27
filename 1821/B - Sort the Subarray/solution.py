t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    i = 0 
    j = n - 1
    arr = []
    while i < n:
        if a[i] != b[i]: 
            arr.append(i+1)
            break
        i+=1
    while j > -1 :
        if a[j] != b[j]:
            arr.append(j+1)
            break
        j-=1
    for k in range(i-1,-1,-1):
        if b[k]<=b[k+1]:
            arr[0]-=1 
        else:
            break 
    for k in range(j+1,n):
        if b[k-1] <= b[k]:
            arr[1]+=1
        else:
            break
    ans.append(arr)
for i in ans:
    print(*i)