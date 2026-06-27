t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    c=n
    pow_2=0
    pow_3=0
    while c%2==0:
        c = c / 2
        pow_2 += 1
    while c%3==0:
        c = c / 3 
        pow_3 += 1
    if c==1:
        if pow_2 <= pow_3 :
            ans.append(2*pow_3-pow_2)
        else:
            ans.append(-1)
    else:
        ans.append(-1)
for i in ans:
    print(i)