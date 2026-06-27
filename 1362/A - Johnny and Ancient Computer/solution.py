t = int(input())
ans = []
for _ in range(t):
    a,  b= map(int,input().split())
    big = max(a,b)
    small = min(a,b)
    count=0
    check=0
    if big % small != 0:
        ans.append(-1)
    else:
        count = big // small
        arr=[8,4,2]
        num=0
        for i in arr:
            while count % i == 0:
                count//=i 
                num+=1
        if count!=1:
            ans.append(-1)
        else:
            ans.append(num)
for i in ans:
    print(i)