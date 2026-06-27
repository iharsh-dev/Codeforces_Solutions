t = int(input())
ans=[]
boool=[]
for _ in range(t):
    x, k = map(int,input().split())
    if x%k==0:
        ans.append([k-1,x-k+1])
    else:
        ans.append([x])
for i in ans:
    print(len(i))
    print(*i)