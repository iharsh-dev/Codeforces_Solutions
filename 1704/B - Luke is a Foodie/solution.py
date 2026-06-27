t = int(input())
ans = []
for _ in range(t):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    L = a[0] - x 
    R = a[0] + x 
    count = 0
    for i in range(1,n):
        newL = a[i] - x
        newR = a[i] + x 
        if max(L,newL) <= min(R,newR):
            L = max(L,newL)
            R = min(R,newR)
        else:
            L = newL
            R = newR 
            count+=1
    ans.append(count)
for i in ans:
    print(i)