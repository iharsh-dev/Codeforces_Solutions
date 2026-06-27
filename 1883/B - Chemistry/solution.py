t=int(input())
ans=[]
for i in range(t):
    n,k=map(int,input().split())
    s=input()
    arr=list(s)
    arr.sort()
    hum=0
    check=1
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            check+=1
        else:
            check=1
        if check%2==0:
            hum+=1
    if n-k%2==0 and 2*hum>=n-k:
        ans.append("YES")
    elif n-k%2!=0 and 2*hum>=n-k-1:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)