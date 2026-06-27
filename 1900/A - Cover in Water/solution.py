t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    s=input()
    arr=list(s)
    con=0
    i=0
    check=0
    while i<n:
        if arr[i]=='.':
            count=0
            while i<n:
                if arr[i]=='.':
                    count+=1 
                    con+=1
                    if count==3:
                        break
                else:
                    break
                i+=1 
            if count==3:
                ans.append(2)
                check+=1
                break
        i+=1 
    if check==0:
        ans.append(con)
for i in ans:
    print(i)