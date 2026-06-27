t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    s=input()
    count=1
    for i in range(n-1):
        if s[i]=='R' and s[i+1]=='L':
            count+=1
            break 
        else:
            count+=1
    ans.append(count)
for i in ans:
    print(i)