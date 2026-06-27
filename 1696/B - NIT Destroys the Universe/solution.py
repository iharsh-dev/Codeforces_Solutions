t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    segment=0
    count=0
    for i in range(n):
        if s[i]!=0:
            if segment==0:
                count+=1
                segment=1
        else:
            segment=0
    if count==0:
        ans.append(0)
    elif count==1:
        ans.append(1)
    else:
        ans.append(2)
for i in ans:
    print(i)