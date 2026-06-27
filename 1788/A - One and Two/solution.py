t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    nos=0
    for i in a:
        if i==2:
            nos+=1
    if nos%2==0:
        nos_2=0
        for i in range(n):
            if a[i]==2:
                nos_2+=1
            if nos_2==nos//2:
                ans.append(i+1)
                break
    else:
        ans.append(-1)
for i in ans:
    print(i)