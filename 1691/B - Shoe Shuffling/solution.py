from collections import Counter
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    frequency=Counter(a)
    check=0
    for i in frequency.values():
        if i==1:
            check=1 
    arr=[]
    k=1
    for i in frequency.values():
        arr.append(k+i-1)
        for j in range(i-1):
            arr.append(k)
            k+=1
        k+=1
    if check==1:
        ans.append([-1])
    else:
        ans.append(arr)
for i in ans:
    print(*i)