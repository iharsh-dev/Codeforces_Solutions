t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    neg=0
    pos=0
    for i in a:
        if i>0:
            pos+=1
        else:
            neg+=1
    if pos>=neg:
        if neg%2==0:
            ans.append(0)
        else:
            ans.append(1)
    else:
        c=(neg-pos+1)//2
        neg-=c 
        pos+=c 
        if neg%2==0:
            ans.append(c)
        else:
            ans.append(c+1)
for i in ans:
    print(i)