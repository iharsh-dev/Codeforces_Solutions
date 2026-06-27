a=int(input())
ans=[]
while a:
    size=int(input())
    num=list(map(int,input().split()))
    C=0
    A=0
    for n in num:
        if n==0:
            C+=1 
        elif n==-1:
            A+=-1
    if A%2==0:
        ans.append(C)
    else:
        ans.append(C+2)
    a-=1
for b in ans:
    print(b)