t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    if n > 1:
        i = 1
        j = n - 2 
        alice = a[0]
        bob = a[-1]
        arr = -1
        while i <= j:
            if alice > bob:
                bob+=a[j]
                j-=1 
            elif bob > alice:
                alice+=a[i]
                i+=1
            else:
                arr = i+n-j-1
                alice+=a[i]
                i+=1
        if alice == bob:
            arr = i+n-j-1
        if arr == -1:
            ans.append(0)
        else:
            ans.append(arr)
    else:
        ans.append(0)
for i in ans:
    print(i)