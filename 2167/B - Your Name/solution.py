a=int(input())
ans=[]
while a:
    b=int(input())
    num=input()
    name=num.split()
    bf=''.join(sorted(name[0]))
    gf=''.join(sorted(name[1]))
    if bf==gf:
        ans.append("YES")
    else:
        ans.append("NO")
    a-=1 
for i in ans:
    print(i)