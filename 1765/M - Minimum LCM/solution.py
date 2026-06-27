import math
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    if n%2==0:
        ans.append([n//2,n//2])
    else:
        arr=[]
        g=1
        for i in range(3,int(math.sqrt(n)+1),2):
            if n%i==0:
                g=n//i 
                break
        ans.append([g,n-g])
for i in ans:
    print(*i)