t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=input()
    b=[int(i) for i in a]
    i=0
    j=n-1
    count=0
    while j>i:
        if b[i]+b[j]==1:
            count+=2
        else:
            break
        i+=1
        j-=1
    ans.append(n-count)
for i in ans:
    print(i)