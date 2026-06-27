t=int(input())
ans=[]
for _ in range(t):
    b,c=input().split()
    n=int(b)
    a=input()
    maxx=[]
    if c=='g':
        ans.append(0)
    else:
        c_dex=-1
        g_dex=-1
        check=0
        for i in range(len(a)):
            if a[i]==c and c_dex== -1:
                c_dex=i
            elif a[i] == 'g':
                if c_dex!=-1:
                    maxx.append(i-c_dex)
                c_dex=-1
                if g_dex==-1:
                    g_dex=i
        if c_dex!=-1:
            maxx.append(g_dex+n-c_dex)
        ans.append(max(maxx))
for i in ans:
    print(i)