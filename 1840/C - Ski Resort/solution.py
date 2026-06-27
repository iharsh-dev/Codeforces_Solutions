t=int(input())
arr=[]
for _ in range(t):
    n,k,q=map(int,input().split())
    a=list(map(int,input().split()))
    ans=[]
    i=0
    while i<n:
        count=0
        while i<n and a[i]<=q:
            count+=1 
            i+=1 
        ans.append(count)
        i+=1
    num=0
    for l in ans:
        if l >= k:
            for j in range(k,l+1):
                num+=(l-j+1)
    arr.append(num)
for i in arr:
    print(i)