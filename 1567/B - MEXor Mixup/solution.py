t = int(input())
ans = []
for _ in range(t) :
    a, b = map(int,input().split())
    count = a 
    n = a-1
    if n % 4 == 0:
        d = n
    elif n % 4 == 1:
        d = 1
    elif n % 4 == 2:
        d = n + 1
    else:
        d = 0
    c = b^(d)
    if c == 0:
        count = a
    elif c == a :
        count += 2 
    else :
        count +=1
    ans.append(count)
for i in ans :
    print(i)