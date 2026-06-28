import sys
input = sys.stdin.readline
 
MAXN = 10**6 + 1
ans = [0] * MAXN
 
for p in range(2, MAXN):
    if ans[p] == 0:  
        for multiple in range(p, MAXN, p):
            n = multiple
            ans[multiple] += 1  
            while n % p == 0:
                ans[multiple] += 1
                n //= p
 
 
t = int(input())
out = []
for _ in range(t):
    n = int(input())
    out.append(ans[n] - 1)
sys.stdout.write('
'.join(map(str, out)) + '
')