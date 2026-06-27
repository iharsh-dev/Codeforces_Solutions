t=int(input())
ans=0
for i in range(t):
    s=list(map(int,input().split()))
    num=0
    for i in s:
        if i==1:
            num+=1 
    if num>=2:
        ans+=1
print(ans)