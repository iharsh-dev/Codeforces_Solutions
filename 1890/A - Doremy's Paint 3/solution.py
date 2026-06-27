t = int(input())
ans=[]
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    arr=[]
    a.sort()
    i=0
    while i<n:
        temp=a[i]
        c=0
        while i<n and a[i]==temp:
            c+=1
            i+=1
        arr.append(c)
    if len(arr)==1:
        ans.append("YES")
    elif len(arr)==2 and (arr[0]==n//2 or arr[1]==n//2):
        ans.append("YES")
    else:
        ans.append("NO")
for i in ans:
    print(i)