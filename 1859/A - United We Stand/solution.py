t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    b=[]
    c=[]
    for i in a:
        if i%2==0:
            c.append(i)
        else:
            b.append(i)
    if len(set(a))==1:
        ans.append(-1)
    elif len(c)==0:
        for i in range(n-1,0,-1):
            c.append(b[i])
            if b[i]!=b[i-1]:
                b=b[:i]
                break
        ans.append(b)
        ans.append(c)
    elif len(b)==0:
        for i in range(n-1):
            b.append(c[i])
            if c[i]!=c[i+1]:
                c=c[i+1:]
                break
        ans.append(b)
        ans.append(c)
    else:
        ans.append(b)
        ans.append(c)
i=0
while i<len(ans):
    if ans[i]!=-1:
        print(len(ans[i]),len(ans[i+1]))
        print(*ans[i])
        print(*ans[i+1])
        i+=2
    else:
        print(ans[i])
        i+=1