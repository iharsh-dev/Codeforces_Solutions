t = int(input())
ans = [] 
for _ in range(t):
    n,x,y,z = map(int,input().split())
    count = 0
    hours = 0
    while count < n :
        count += (x+y) 
        hours+=1 
    count = 0
    hours_ = 0
    while count < n :
        if hours_ < z :
            count += x 
        else:
            count += (x+y*10)
        hours_+=1 
    ans.append(min(hours_,hours))
for i in ans:
    print(i)