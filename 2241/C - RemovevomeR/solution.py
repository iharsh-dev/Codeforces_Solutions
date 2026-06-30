t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    runs = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            runs += 1
    
    ans = 2 if runs == 2 else 1
    print(ans)