m,n=map(int,input().split())
a=min(m,n)
b=max(m,n)
ans=a//2*b+a%2*b//2
print(ans)