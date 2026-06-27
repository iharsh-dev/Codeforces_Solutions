t = int(input())
ans=[]
boool=[]
for _ in range(t):
    n = int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    check=0
    if a[0]==a[1]:
        for i in range(2,n):
            if a[0]!=a[i]:
                check=1
                a[0],a[i]=a[i],a[0]
    else:
        check=1
    if check:
        boool.append(True)
        ans.append(a)
    else:
        boool.append(False)
        ans.append([0])
        
for i in range(t):
    if boool[i]:
        print('Yes')
        print(*ans[i])
    else:
        print('NO')