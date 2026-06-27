t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    even=0
    odd=0
    for i in a:
        if i%2==0:
            even+=1 
        else:
            odd+=1 
    if odd%2==0:
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)