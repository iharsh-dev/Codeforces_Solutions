t = int(input())
ans=[]
for _ in range(t):
    n, r, b = map(int,input().split())
    red = r//(b+1)
    left = r - red*(b+1)
    s = ""
    yes = ''
    for i in range(red):
        yes+='R'
    for i in range(b):
        if left:
            s+=(yes+'RB')
            left-=1
        else:
            s+=(yes+'B')
    s+=yes 
    ans.append(s)
for i in ans:
    print(i)