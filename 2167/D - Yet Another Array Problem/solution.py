import math
a=int(input())
ans=[]
while a:
    input()
    num=list(map(int,input().split()))
    i=min(num)
    if any(x%2!=0 for x in num):
        ans.append(2)
    else:
        check=0
        for j in range(3,1000000000,2):
            if any(math.gcd(x,j)==1 for x in num):
                check=1
                ans.append(j)
                break
        if check==0:
            ans.append(-1)
    a-=1 
for i in ans:
    print(i)