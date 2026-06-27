t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    count=0
    i=1
    while True:
        if n<i*10:
            count = count + n//i
            break
        else:
            count+=9
        i*=10 
    ans.append(count)
for i in ans:
    print(i)