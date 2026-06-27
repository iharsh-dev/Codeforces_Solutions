import sys
t = int(input())
ans = []
for _ in range(t):
    n, k, a, b = map(int,input().split())
    major = []
    minor = []
    for i in range(k):
        x, y = map(int,input().split())
        major.append([x,y])
    for i in range(n-k):
        x, y = map(int,input().split())
        minor.append([x,y])
    dist = 0
    if a > k :
        x = minor[a-k-1][0]
        y = minor[a-k-1][1]
        minn = sys.maxsize
        for i in major:
            minn = min(abs(x-i[0])+abs(y-i[1]),minn)
        dist += minn
    if b > k:
        x = minor[b-k-1][0]
        y = minor[b-k-1][1]
        minn = sys.maxsize
        for i in major:
            minn = min(abs(x-i[0])+abs(y-i[1]),minn)
        dist += minn
    direct = sys.maxsize
    if a > k and b > k:
        direct = abs( minor[a-k-1][0]-minor[b-k-1][0])+abs(minor[a-k-1][1]-minor[b-k-1][1])
    ans.append(min(direct,dist))
for i in ans:
    print(i)