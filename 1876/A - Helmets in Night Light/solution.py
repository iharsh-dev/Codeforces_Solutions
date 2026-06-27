t = int(input())
ans = []
for _ in range(t) :
    n, p = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split())) 
    new = list(zip(a,b))
    new_sort = sorted(new, key=lambda x: (x[1], -x[0])) 
    count = 1 
    price = p
    i = 0
    while count < n :
        if new_sort[i][1] < p :
            if count + new_sort[i][0] <= n :
                count+=new_sort[i][0]
                price+=(new_sort[i][0]*new_sort[i][1])
            else:
                price+=((n - count)*new_sort[i][1])
                count = n 
        else:
            count +=1 
            price+=p 
        i+=1
    ans.append(price)
for i in ans:
    print(i)