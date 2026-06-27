t=int(input())
ans=[]
for _ in range(t):
    n,k=map(int,input().split())
    a=[]
    rev=[]
    for i in range(n):
        b=list(map(int,input().split()))
        a.append(b)
    for i in range(n-1,n//2-1,-1):
        b=a[i][:]
        b.reverse()
        rev.append(b)
    count=0
    if n%2==0:
        for i in range(len(rev)):
            for j in range(n):
                if a[i][j]!=rev[i][j]:
                    count+=1
    else:
        for i in range(len(rev)-1):
            for j in range(n):
                if a[i][j]!=rev[i][j]:
                    count+=1
        for i in range(n//2):
            if a[n//2][i]!=rev[-1][i]:
                count+=1
    if count==k:
        ans.append("YES")
    elif count<k:
        if n%2==0:
            if (k-count)%2==0:
                ans.append("YES")
            else:
                ans.append("NO")
        else:
            ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)