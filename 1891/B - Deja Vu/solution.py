from collections import defaultdict
 
t = int(input())
ans = []
 
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = list(map(int, input().split()))
 
    arr = defaultdict(list)
 
    for i in range(n):
        arr[(a[i] & -a[i]).bit_length() - 1].append((a[i], i))
 
    for i in q:
        target = i - 1
 
        for k in list(arr.keys()):
            if k >= i:
                for val, idx in arr[k]:
                    arr[target].append((val + (1 << target), idx))
                arr[k].clear()
 
    crr = [0] * n
 
    for k in arr:
        for val, idx in arr[k]:
            crr[idx] = val
 
    ans.append(crr)
 
for x in ans:
    print(*x)