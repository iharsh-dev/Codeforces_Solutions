n=int(input())
a=input()
b=list(a)
c=b[:]
c.sort()
d="".join(c)
if a==d:
    print("NO")
else:
    ans=[]
    i=0
    while i<n:
        if a[i]!=c[i]:
            break
        i+=1
    o=i+1 
    e=b[i+1:]
    p=e.index(min(e))+o+1
    print("YES")
    print(o,p)