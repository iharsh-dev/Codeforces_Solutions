a=int(input())
ans=[]
while a:
    b=int(input())
    num=list(map(int,input().split()))
    count=0
    i=0
    while i<max(num)+1:
        if i in num:
            count+=1 
        i+=1
    ans.append(count)
    a-=1 
for i in ans:
    print(i)