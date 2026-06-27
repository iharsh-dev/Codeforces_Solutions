t = int(input())
ans = []
for _ in range(t):
    x, y, k = map(int,input().split())
    need = k*(1+y)
    a = 1
    i=0
    while a < need :
        a*=x
        i+=1
    arr=0
    for j in range(i-1):
        arr+=(x**j)
    rn=(x**(i-1))
    if (need-rn)%(x-1)==0:
        arr+=(need-rn)//(x-1) 
    else:
        arr+=(need-rn)//(x-1)+1
    ans.append(arr+k)
for i in ans:
    print(i)