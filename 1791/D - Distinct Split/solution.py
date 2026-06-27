t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=input()
    b=[ord(i) for i in a]
    mapp1=[0]*123
    mapp2=[0]*123
    forw=[]
    back=[]
    num=0
    for i in range(n):
        if mapp1[b[i]]==0:
            mapp1[b[i]]=1 
            num+=1
        forw.append(num)
    num=0
    for i in range(n-1,-1,-1):
        if mapp2[b[i]]==0:
            mapp2[b[i]]=1 
            num+=1
        back.append(num)
    maxx=[]
    back.pop()
    forw.pop()
    back.reverse()
    for i in range(n-1):
        maxx.append(forw[i]+back[i])
    ans.append(max(maxx))
for i in ans:
    print(i)