t=int(input())
ans=[]
for _ in range(t):
    a, b, c, d = map(int,input().split())
    x=abs(a-c)
    y=abs(b-d)
    if b-d>0:
        ans.append(-1)
    elif b-d==0:
        if a-c>=0:
            ans.append(x)
        else:
            ans.append(-1)
    else:
        if x==y:
            if a-c<=0:
                ans.append(x)
            else:
                ans.append(3*x)
        elif x<y:
            if a-c<=0:
                ans.append(2*y-x)
            else:
                ans.append(2*y+x)
        else:
            if a-c>=0:
                ans.append(x+2*y)
            else:
                ans.append(-1)
for i in ans:
    print(i)