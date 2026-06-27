t=int(input())
ans=[]
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    arr=[]
    som=[0]*(n+1)
    for i in range(n):
        som[i+1]=som[i]+a[i]
    for i in range(k+1):
        arr.append(som[n-k+i]-som[2*i])
    ans.append(max(arr))
for i in ans:
    print(i)