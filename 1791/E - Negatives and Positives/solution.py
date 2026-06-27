t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    neg = 0
    zero = 0
    for i in range(n):
        if a[i] < 0:
            neg+=1 
            a[i] = -1*a[i] 
        elif a[i] == 0:
            zero += 1 
    some = sum(a)
    if neg%2 != 0 and zero == 0:
        ans.append(some - 2*min(a))
    else:
        ans.append(some)
for i in ans:
    print(i)