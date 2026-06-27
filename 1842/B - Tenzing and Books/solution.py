t = int(input())
ans = []
for _ in range(t):
    n, x = map(int,input().split())
    arr = []
    for i in range(3):
        a = list(map(int,input().split()))
        arr.append(a)
    if x==0:
        ans.append('Yes')
    else:
        arm =0
        for i in range(3):
            for j in range(n):
                if (x|arr[i][j]) != x:
                    break 
                else:
                    arm = arm|arr[i][j]
        if arm == x:
            ans.append('Yes')
        else:
            ans.append('No')
for i in ans:
    print(i)