t=int(input())
ans=[]
for _ in range(t):
    n, m = map(int,input().split())
    a = input()
    b = input()
    i=0
    check=0
    c=0
    while n<m:
        c+=1
        n=2*n
    for j in range(c+2):
        if b not in a:
            a=a+a
        else:
            check=1
            break
        i+=1
    if check:
        ans.append(i)
    else:
        ans.append(-1)
for i in ans:
    print(i)