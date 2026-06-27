t=int(input())
ans=[]
for _ in range(t):
    target=[]
    for i in range(10):
        a=input()
        target.append(a)
    score=0
    for i in range(10):
        for j in range(10):
            if target[i][j]=='X':
                c=i
                d=j
                if i>4:
                    c=9-i
                if j>4:
                    d=9-j
                prod=c*d 
                if c==d:
                    score+=(c+1)
                elif prod==0:
                    score+=1
                elif 1<prod<=4:
                    score+=2
                elif 4<prod<9:
                    score+=3
                elif 9<prod<16:
                    score+=4
    ans.append(score)
for i in ans:
    print(i)