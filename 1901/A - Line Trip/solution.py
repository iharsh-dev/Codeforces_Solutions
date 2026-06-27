t=int(input())
ans=[]
for i in range(t):
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    diff=[]
    diff.append(x[0])
    for i in range(n-1):
        diff.append(x[i+1]-x[i])
    diff.append(2*(k-x[-1]))
    ans.append(max(diff))
for i in ans:
    print(i)