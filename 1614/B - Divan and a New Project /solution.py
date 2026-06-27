t = int(input())
ans1 = []
ans = []
for _ in range(t) :
    n = int(input())
    a = list(map(int,input().split()))
    d = {}
    for i in range(n):
        d[i] = a[i]
    sorted_d = dict(sorted(d.items(), key=lambda x: x[1], reverse = True))
    arr = [0] 
    i = 0
    j = 0
    count = 0
    for key in sorted_d :
        if count%2==0:
            i-=1
            sorted_d[key] = i
            count +=1
        else:
            j+=1
            sorted_d[key] = j
            count+=1
    for i in range(n):
        arr.append(sorted_d[i])
    count = 0
    for i in range(n) :
        count+=a[i]*2*abs(arr[i+1])
    ans1.append(count)
    ans.append(arr)
for i in range(len(ans)) :
    print(ans1[i])
    print(*ans[i])