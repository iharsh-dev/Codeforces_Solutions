t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    tasks=[]
    for i in range(n):
        a=list(map(int,input().split()))
        tasks.append(a)
    s=0.0
    for i in range(n-1,-1,-1):
        skip=s 
        done=tasks[i][0]+(1-tasks[i][1]/100)*s
        s=max(skip,done)
    ans.append(s)
for i in ans:
    print(f"{i:9f}")