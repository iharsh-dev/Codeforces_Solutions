t=int(input())
ans=[]
for i in range(t):
    b=int(input())
    a=list(map(int,input().split()))
    c=max(a)
    a.sort()
    d=a.index(c)
    ans.append(b-d)
for i in ans:
    print(i)