t=int(input())
ans=[]
mod = 10**9+7
INV6 = 166666668
for _ in range(t):
    n = int(input())
    arr=n * (n+1) % mod
    arr=arr * (4*n-1) % mod
    arr=arr * INV6 % mod
    arr=arr * 2022 % mod
    ans.append(arr)
for i in ans:
    print(i)