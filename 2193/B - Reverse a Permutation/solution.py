t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    a=list(map(int,input().split()))
    for i in range(0,n):
        if a[i]==n-i:
            ans.append(n-i)
        else:
           b=a.index(n-i)
           c=a[i:b+1]
           c.reverse()
           ans=ans+c+a[b+1:]
           break
    print(*ans)