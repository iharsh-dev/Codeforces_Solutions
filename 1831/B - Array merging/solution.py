t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    da = {x: 0 for x in set(a+b)}
    db = {x: 0 for x in set(a+b)}
    c = set(a+b)
    arr =[]
    i = 0
    while i < n:
        curr = a[i]
        count = 0
        while i < n and curr == a[i]:
            count+=1 
            i+=1
        if count > da[curr] :
            da[curr] = count
    i = 0
    while i < n:
        curr = b[i]
        count = 0
        while i < n and curr == b[i]:
            count+=1 
            i+=1
        if count > db[curr] :
            db[curr] = count 
    for i in c:
        arr.append(da[i]+db[i])
    ans.append(max(arr))
for i in ans:
    print(i)