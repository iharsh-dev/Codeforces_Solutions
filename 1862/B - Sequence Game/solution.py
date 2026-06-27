t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    arr=[a[0]]
    count=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            b=a[i+1]
            arr.append(b)
        arr.append(a[i+1])
    ans.append(arr)
for i in ans:
    print(len(i))
    print(*i)