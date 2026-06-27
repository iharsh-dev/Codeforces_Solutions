n,k=map(int,input().split())
arr=list(map(int,input().split()))
tar=arr[k-1]
num=0
for i in arr:
    if i>0:
        if i>=tar:
            num+=1 
print(num)