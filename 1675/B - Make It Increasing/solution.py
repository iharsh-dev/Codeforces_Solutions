import math
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    count=0
    ok=True
    for i in range(n-2,-1,-1):
        while s[i]>=s[i+1]:
            if s[i+1]==0:
                ok=False
                break
            diff = s[i]//s[i+1]
            steps = max(1, diff.bit_length() - 1)
    
            s[i] >>= steps
            count += steps
            if s[i]>=s[i+1]:
                s[i]=s[i]//2
                count+=1
            if s[i] == 0 and s[i] >= s[i+1]:
                ok = False
                break
    ans.append( count if ok else -1)
for i in ans:
    print(i)
    