t = int(input())
ans = []
for _ in range(t):
    a, b = map(int,input().split())
    current = 0
    prev = 0
    i = 0
    if b == 1:
        b+=1 
        prev +=1
        i += 1
    n = a
    while a != 0:
        a = a//b
        prev += 1
    while True:
        b += 1
        i+=1
        current = i
        a = n
        while a!=0:
            a = a//b 
            current +=1
        if current > prev :
            break 
        else:
            prev = current
    ans.append(prev)
for i in ans:
    print(i)