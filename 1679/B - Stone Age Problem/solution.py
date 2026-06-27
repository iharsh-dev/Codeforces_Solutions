n, q = map(int,input().split())
a=list(map(int,input().split()))
som=sum(a)
ans=[]
check=0
for _ in range(q):
    t=list(map(int,input().split()))
    if t[0]==1:
        if check:
            if dic.get(t[1],False):
                temp=dic[t[1]]
                dic[t[1]]=t[-1]
                som = som - temp + t[-1]
            else:
                dic[t[1]]=t[-1]
                som = som - dic[-1] + t[-1]
        else:
            temp=a[t[1]-1] 
            a[t[1]-1]=t[2]
            som = som-temp+t[2]
    else:
        check=1
        dic={-1:t[-1]}
        som=t[-1]*n 
    ans.append(som)
for i in ans:
    print(i)