from collections import Counter
t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse = True)
    freq = Counter(a)
    check = True
    for i in freq.values():
        if i != 1 :
            check = False
            break
    if check:
        ans.append(a)
    else:
        ans.append([-1])
for i in ans:
    print(*i)