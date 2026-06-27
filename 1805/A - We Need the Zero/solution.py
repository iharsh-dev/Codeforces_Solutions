t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    b=0
    for i in a:
        b = b^i
    if b==0:
        ans.append(0)
    else:
        if n%2==0:
            ans.append(-1)
        else:
            ans.append(b)
for i in ans:
    print(i)