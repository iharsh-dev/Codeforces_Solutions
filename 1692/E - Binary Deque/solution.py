t = int(input())
ans = []
for _ in range(t):
    n, s = map(int,input().split())
    arr = list(map(int,input().split()))
    some = sum(arr)
    if some < s:
        ans.append(-1)
    elif some == s:
        ans.append(0)
    else:
        i = 0
        count = 0
        maxx = 0
        for j in range(n):
            count+=arr[j]
            while count > s:
                count-=arr[i]
                i+=1 
            if count == s:
                maxx=max(maxx,j-i+1)
        ans.append(n-maxx)
for i in ans:
    print(i)