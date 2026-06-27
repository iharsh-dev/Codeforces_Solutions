import math
t = int(input())
ans = []
for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input()
    arr = []
    x = 0
    count = 0
    for i in s:
        if i == c:
            count+=1
    if count != n:
        for i in range(n//2,n):
            if s[i] == c:
                x = i+1 
                break
        if x:
            arr.append(x)
        else:
            arr.append(n-1)
            arr.append(n)
    ans.append(arr)
for i in ans:
    print(len(i))
    if len(i)!=0:
        print(*i)