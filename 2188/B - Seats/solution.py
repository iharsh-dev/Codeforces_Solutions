t=int(input())
ans=[]
#fuck
for i in range(t):
    n=int(input())
    s=input()
    ss=list(s)
    arr=[]
    diff=[]
    stu=0
    for i in range(n):
        if ss[i]=='1':
            arr.append(i)
    
    if len(arr)>0:
        for i in range(len(arr)-1):
            f=arr[i+1]-arr[i]-1
            diff.append(f)
        for i in diff:
            stu+=i//3
        stu+=(arr[0]+1)//3
        stu+=((n-arr[-1]-1)+1)//3
        ans.append(stu+len(arr))
    else:
        d=(n+2)//3
        ans.append(d)
for i in ans:
    print(i)