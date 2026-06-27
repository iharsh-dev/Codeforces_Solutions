t = int(input())
ans=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    count=0
    i=0
    while i<n-1-count:
        if a[i]%2==0 and a[i+1]%2==0:
            a[i]=a[i]*a[i+1]
            a.pop(i+1)
            count+=1
        elif a[i]%2!=0 and a[i+1]%2!=0:
            a[i]=a[i]*a[i+1]
            a.pop(i+1)
            count+=1
        else:
            i+=1
    ans.append(count)
for i in ans:
    print(i)