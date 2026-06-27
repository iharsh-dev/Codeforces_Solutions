t = int(input())
ans=[]
for _ in range(t):
    a, b, c = map(int,input().split())
    if c%2==0:
        if a<=b:
            ans.append('Second')
        else:
            ans.append('First')
    else:
        if a>=b:
            ans.append('First')
        else:
            ans.append('Second')
for i in ans:
    print(i)