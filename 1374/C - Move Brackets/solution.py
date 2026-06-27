t = int(input())
ans = []
for _ in range(t):
    n = int(input())
    s = input()
    a=[]
    for i in s:
        if i=='(':
            a.append('(')
        else:
            if len(a)>0 and a[-1] == '(':
                a.pop()
            else:
                a.append(')')
    ans.append(len(a)//2)   
for i in ans:
    print(i)