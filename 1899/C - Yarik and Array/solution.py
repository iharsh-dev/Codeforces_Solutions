t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n <= 1:
        ans.append(a[-1])
    else:
        i = 0
        j = 0
        maxxx = - (10**3+1)
        curr = a[0]
        maxx = a[0]
        while j < n-1 :
            if (a[j]&1)^(a[j+1]&1):
                curr = max(a[j+1], curr + a[j+1])
                maxx = max(maxx, curr)   
                j+=1 
            else:
                maxxx = max(maxx,maxxx)
                j+=1
                i = j
                curr = a[i]
                maxx = a[i]
        maxxx = max(maxx,maxxx)
        ans.append(maxxx)
for i in ans:
    print(i)