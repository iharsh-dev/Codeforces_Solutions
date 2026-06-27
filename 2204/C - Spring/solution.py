import math
t=int(input())
ans=[]
for _ in range(t):
    a,b,c,m=map(int,input().split())
    a_b_c=math.lcm(a,b,c)
    a_b=math.lcm(a,b)
    a_c=math.lcm(a,c)
    b_c=math.lcm(b,c)
    Alice=0
    Bob=0
    Carol=0
    p=m//a_b_c
    q=m//a_b
    r=m//a_c
    s=m//b_c
    t=m//a 
    u=m//b 
    v=m//c
    Alice=2*p+3*(q-p+r-p)+6*(t+p-q-r)
    Bob=2*p+3*(q-p+s-p)+6*(u+p-q-s)
    Carol=2*p+3*(r-p+s-p)+6*(v-r-s+p)
    ans.append([Alice,Bob,Carol])
for i in ans:
    print(*i)