t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range(n):
        if a[i]>i+1:
            continue
        else:
            count+=1
    ans.append(count)
for i in ans:
    print(i)