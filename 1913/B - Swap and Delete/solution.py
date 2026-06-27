t=int(input())
ans=[]
for _ in range(t):
    a = input()
    b = [int(i) for i in a]
    c=len(b)
    one=sum(b)
    zero=c-one
    num_1=[0]*c
    num_0=[0]*c
    m=0
    for i in range(c):
        m+=b[i]
        num_1[i]=m 
        num_0[i]=i-m+1
    if c==one or one==0:
        ans.append(c)
    for i in range(c-1,-1,-1):
        if num_1[i]==zero and num_0[i]==one:
            ans.append(c-i-1)
            break
        elif num_1[i]>=zero:
            one-=1
        elif num_0[i]>=one:
            zero-=1 
for i in ans:
    print(i)