t = int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans.append(-1*sum(a))
for i in ans:
    print(i)