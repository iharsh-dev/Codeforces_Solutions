t = int(input())
ans = []
for _ in range(t) :
    n = int(input())
    arr = [] 
    for i in range(n) :
        arr.append(i+1)
    if n%2==0:
        arr_ = arr[::-1]
        brr = arr + arr_ + arr + arr 
        ans.append(brr)
    else:
        arr_ = arr[1:]+arr[:1]
        arr1 = arr[::-1]
        arr2 = arr_[::-1]
        brr = arr + arr1 + arr_ + arr2
        ans.append(brr)
for i in ans:
    print(*i)