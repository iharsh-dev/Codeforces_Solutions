t=int(input())
ans=[]
for _ in range(t):
    n , x = map(int,input().split())
    a=list(map(int,input().split()))
    b=a[:]
    b.sort()
    count=0
    i=0
    height=0
    done=False
    while i < n-1:
        c=(i+1)*(b[i+1]-b[i])
        if c+count>x:
            m=((x-count)//(i+1))
            count+=(i+1)*m
            height=b[i]+m
            ans.append(height)
            done=True
            break
        else:
            count+=c 
            height=b[i+1]
        i+=1
    if not done:
        ans.append(max(b)+(x-count)//n)
for i in ans:
    print(i)