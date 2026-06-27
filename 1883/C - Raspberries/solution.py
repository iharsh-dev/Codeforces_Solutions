t = int(input())
ans=[]
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    if k!=4:
        need=k
        for i in range(n):
            for j in range(1,6):
                if a[i]<=j*k:
                    if need > k*j-a[i]:
                        need=k*j-a[i]
                        break
        ans.append(need)
    else:
        need_2=[2,2]
        need_4=k
        for i in range(n):
            for j in range(1,6):
                if a[i]<=j*2:
                    if max(need_2) >= 2*j-a[i]:
                        need_2[need_2.index(max(need_2))]=2*j-a[i]
                        break
        for i in range(n):
            for j in range(1,5):
                if a[i]<=j*k:
                    if need_4 > k*j-a[i]:
                        need_4 =k*j-a[i]
                        break            
        ans.append(min(need_4,sum(need_2)))                
for i in ans:
    print(i)