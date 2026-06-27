t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    maxx=0
    for i in range(n):
        count=0
        while i < n and a[i]==0:
            count+=1
            i+=1
        if count>maxx:
            maxx=count
    ans.append(maxx)
for i in ans:
    print(i)