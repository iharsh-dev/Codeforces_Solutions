import math
t = int(input())
ans = []
for _ in range(t):
    n, c = map(int,input().split())
    a = list(map(int,input().split()))
    some = sum(a) 
    sq = sum(x*x for x in a)
    w = (math.sqrt(some*some - n*(sq - c)) - some)// (2*n) 
    ans.append(int(w))
for i in ans:
    print(i)