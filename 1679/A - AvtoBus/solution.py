t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    m = n
    a =[]
    maxx = 0
    minn = 0
    if n % 2!=0:
        a.append(-1)
    else :
        minn = n//6 
        while minn >= 0 and ( n - 6 *minn) % 4 !=0:
            minn-=1 
        maxx = n//4 
        while maxx >= 0 and ( n - 4 * maxx ) % 6 !=0:
            maxx -=1 
        if maxx < 0 or minn < 0:
            a.append(-1)
        else : 
            a.append(minn + (n - 6*minn)//4)
            a.append(maxx + (n -4*maxx)//6)
    ans.append(a)
for i in ans:
    print(*i)