import sys
input = sys.stdin.readline
 
def solve():
    n = int(input())
    parents = list(map(int, input().split()))  
    
    children = [[] for _ in range(n + 1)]
    for i, p in enumerate(parents, start=2):
        children[p].append(i)
    
    depth = [0] * (n + 1)
    max_depth = [0] * (n + 1)
    
    for v in range(1, n + 1):
        max_depth[v] = depth[v]
        for c in children[v]:
            depth[c] = depth[v] + 1
    
    for v in range(n, 0, -1):
        max_depth[v] = depth[v]
        for c in children[v]:
            max_depth[v] = max(max_depth[v], max_depth[c])
    
    ans = n
    for v in range(1, n + 1):
        if len(children[v]) < 2:
            continue
        first = second = -1
        for c in children[v]:
            md = max_depth[c]
            if md > first:
                second = first
                first = md
            elif md > second:
                second = md
        ans += max(0, second - depth[v])
    
    print(ans)
 
t = int(input())
for _ in range(t):
    solve()