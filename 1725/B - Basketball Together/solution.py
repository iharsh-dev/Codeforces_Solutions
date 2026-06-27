n ,d = map(int,input().split())
a = list(map(int,input().split()))
a.sort(reverse=True)
left=n
count=0
i=0
while left>0:
    if d >= a[i]:
        if left >= d//a[i]+1:
            left-=(d//a[i]+1)
        else:
            break
    else:
        left-=1
    count+=1
    i+=1
print(count)