t=int(input())
ans=[]
for _ in range(t):
    a=input()
    arr=[int(i) for i in a]
    n=len(arr)
    for i in range(n//2+1):
        j=0
        check=0
        while j<n-1:
            if arr[j]+arr[j+1]==1:
                del arr[j:j+2]
                n-=2
                check=1
                break
            j+=1
        if check==0:
            if i%2==0:
                ans.append('NET')
            else:
                ans.append('DA')
            break
for i in ans:
    print(i)