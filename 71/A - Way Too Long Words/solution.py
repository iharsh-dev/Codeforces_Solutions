t=int(input())
ans=[]
for i in range(t):
    s=input()
    t=len(s)-2
    if t>8:
        c=s[0]+str(t)+s[-1]
        ans.append(c)
    else:
        ans.append(s)
for i in ans:
    print(i)