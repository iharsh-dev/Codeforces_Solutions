from collections import defaultdict
t = int(input())
ans = []
for _ in range(t):
    n, x, y = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    count = 0
    dicti = defaultdict(int)
    for i in a:
        rx = i%x 
        ry = i%y  
        
        count+=dicti[((x-rx)%x,ry)]
        dicti[(rx,ry)]+=1
    ans.append(count)
for i in ans:
    print(i)