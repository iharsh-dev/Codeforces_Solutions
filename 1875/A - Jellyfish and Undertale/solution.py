t=int(input())
ans=[]
for i in range(t):
    a,b,n=map(int,input().split())
    x=list(map(int,input().split()))
    x.sort()
    time=b
    for xi in x:
        time+=min(xi,a-1)
    ans.append(time)
for i in ans:
    print(i)