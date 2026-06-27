import math
t = int(input())
ans = []
for _ in range(t) :
    d = int(input())
    p = d + 1 
    while True :
        if p == 2 :
            break 
        elif p % 2 == 0 :
            p+=1 
        else :
            check = True
            for i in range(3,int(math.sqrt(p)) + 1, 2) :
                if p % i == 0 :
                    check = False 
                    break 
            if check :
                break 
            else :
                p += 1
    q = p + d 
    while True :
        if q == 2 :
            break 
        elif q % 2 == 0 :
            q+=1 
        else :
            check = True
            for i in range(3,int(math.sqrt(q)) + 1, 2) :
                if q % i == 0 :
                    check = False 
                    break 
            if check :
                break 
            else :
                q += 1
    ans.append(p*q)
for i in ans:
    print(i)