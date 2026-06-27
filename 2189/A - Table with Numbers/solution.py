t=int(input())
ans=[]
for i in range(t):
    n,h,l=map(int,input().split())
    x=0
    y=0
    arr=list(map(int,input().split()))
    for j in arr:
        if j<=min(h,l):
            x+=1 
        elif j<=max(h,l):
            y+=1 
    if y<x:
        ans.append(y+(x-y)//2)
    else:
        ans.append(x)
for j in ans:
    print(j)