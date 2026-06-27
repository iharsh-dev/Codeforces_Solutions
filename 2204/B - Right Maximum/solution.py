t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    count=1
    maxx=s[0]
    for i in range(1,n):
        if s[i]>=maxx:
            count+=1
            maxx=s[i]
    ans.append(count)
for i in ans:
    print(i)