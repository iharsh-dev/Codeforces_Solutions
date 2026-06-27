t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    j = n-1
    maxx = n 
    minn = 1
    while j-i > 2:
        if a[i]==minn:
            minn+=1 
            i+=1 
        elif a[i]==maxx:
            maxx-=1 
            i+=1
        elif a[j]==minn:
            minn+=1 
            j-=1
        elif a[j]==maxx:
            maxx-=1 
            j-=1 
        else:
            ans.append([i+1,j+1])
            break
    if j-i <= 2:
        ans.append(-1)
for i in ans:
    if i==-1:
        print(i)
    else:
        print(*i)