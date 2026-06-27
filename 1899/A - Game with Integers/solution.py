t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    if n%3==0:
        ans.append("Second")
    else:
        ans.append("First")
for i in ans:
    print(i)