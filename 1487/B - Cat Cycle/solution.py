t = int(input())
ans = []
for _ in range(t):
    n, k = map(int,input().split())
    if n % 2 == 0:
        a = k%n if k%n!=0 else n 
        ans.append(a)
    else:
        l = n*(n//2)
        k = k%l if k%l!=0 else l
        add = (k-1)// (n//2)
        ans.append((k+add)%n if (k+add)%n!=0 else n)
for i in ans:
    print(i)