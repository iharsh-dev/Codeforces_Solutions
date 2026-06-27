t=int(input())
ans=[]
for i in range(t):
    n,x=map(int,input().split())
    arr=[]
    l = []
    m = []
    for j in range(n):
        b=list(map(int,input().split()))
        arr.append(b)
    for j in range(n):
        l.append((arr[j][0]*arr[j][1])-arr[j][2])
        m.append(arr[j][0]*(arr[j][1]-1))
    target = x - sum(m)
    anss = 0
    if max(l)<1 and target>0:
        ans.append(-1)
    elif target<=0:
        ans.append(0)
    else:
        if target%max(l) == 0:
            ans.append(target//max(l))
        else:
            ans.append((target//max(l))+1)
for j in ans:
    print(j)
    