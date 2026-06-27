t=int(input())
for i in range(t):
    n=int(input())
    ans=[0]*n
    b=n-1
    j=1
    while True:
        if b>=0:
            ans[b]=j
            b-=2
            j+=1
        else:
            break
    if n%2==0:
        a=0
    else:
        a=1
    while True:
        if a<=n-1:
            ans[a]=j
            a+=2
            j+=1
        else: 
            break
    print(*ans)