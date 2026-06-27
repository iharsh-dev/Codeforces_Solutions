t = int(input())
ans=[]
boool=[]
for _ in range(t):
    n, k, x = map(int,input().split())
    if x!=1:
        boool.append(True)
        a=[1]*n 
        ans.append(a)
    else:
        if n%2==0:
            if k>=2:
                a=[2]*(n//2)
                boool.append(True)
                ans.append(a)
            else:
                boool.append(False)
                ans.append([0])
        else:
            if k>=3:
                boool.append(True)
                a=[2]*(n//2-1)
                a.append(3)
                ans.append(a)
            else:
                boool.append(False)
                ans.append([0])
for i in range(len(ans)):
    if boool[i]:
        print('Yes')
        print(len(ans[i]))
        print(*ans[i])
    else:
        print('NO')