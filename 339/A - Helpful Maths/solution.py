t=input()
ss=t.split("+")
ss.sort()
for i in range(len(ss)):
    if i==len(ss)-1:
        print(ss[i],end="")
    else:
        print(ss[i]+"+",end="")