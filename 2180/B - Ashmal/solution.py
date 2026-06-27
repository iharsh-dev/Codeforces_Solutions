t=int(input())
ans=[]
for i in range(t):
    b=int(input())
    c=input()
    strr=c.split()
    s=""
    s+=strr[0]
    for i in range(1,len(strr)):
        l=strr[i]+s
        r=s+strr[i]
        if l>=r:
            s+=strr[i]
        else:
            s=strr[i]+s
    ans.append(s)
for i in ans:
    print(i)