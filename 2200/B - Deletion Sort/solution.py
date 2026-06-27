t=int(input())
ans=[]
for i in range(t):
    b=int(input())
    a=list(map(int,input().split()))
    b=a[:]
    b.sort()
    if len(a)==1:
        ans.append(1)
    elif b==a:
        ans.append(len(a))
    else:
        ans.append(1)
for i in ans:
    print(i)