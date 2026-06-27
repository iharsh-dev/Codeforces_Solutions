t=int(input())
ans=[]
for i in range(t):
    l,a,b=map(int,input().split())
    arr=[0]*l
    arr.append(a)
    if (l-1-a)%b==0:
        ans.append(l-1)
    else:
        while True:
            a=(a+b)%l
            if arr[a]==1:
                break
            else:
                arr[a]=1 
        for i in range(l-1,-1,-1):
            if arr[i]==1:
                ans.append(i)
                break
for i in ans:
    print(i)