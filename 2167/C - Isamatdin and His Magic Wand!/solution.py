a=int(input())
matrix=[]
for i in range(a):
    b=int(input())
    num=list(map(int,input().split()))
    check=0
    for n in num:
        if n%2==0 :
            check+=1
    if check==len(num) or check==0:
        matrix.append(num)
    else :
        num.sort()
        matrix.append(num)
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print("
") 