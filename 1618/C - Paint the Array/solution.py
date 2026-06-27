import math
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    odd = a[::2]
    even = a[1::2]
    g1 = even[-1]
    g2 = odd[-1]
    for i in even:
        g1 = math.gcd(g1,i)
    for i in odd:
        g2 = math.gcd(g2,i)
    check = True
    for i in odd:
        if i%g1 == 0:
            check = False
            break 
    if check:
        ans.append(g1)
    else:
        check = True
        for i in even:
            if i%g2 == 0:
                check = False
                break 
        if check:
            ans.append(g2)
        else:
            ans.append(0)
for i in ans:
    print(i)