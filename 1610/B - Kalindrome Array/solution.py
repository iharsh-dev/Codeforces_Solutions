t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    i = 0
    j = n - 1 
    arr = []
    chuck = False
    while i < j :
        if a[i] != a[j] :
            chuck = True
            arr.append(a[i])
            arr.append(a[j])
            break 
        i+=1
        j-=1
    if chuck :
        brr = [ x for x in a if x != arr[0]]
        crr = [ x for x in a if x != arr[1]]
        if brr == brr[::-1]:
            check = 'YES' 
        elif crr == crr[::-1]:
            check = 'YES'
        else:
            check = 'NO'
        ans.append(check)
    else:
        ans.append('Yes')
for i in ans:
    print(i)