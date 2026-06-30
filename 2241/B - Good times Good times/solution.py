t = int(input())
ans = []
for _ in range(t):
    a = input()
    d = 0
    for i in a:
        d+=1 
    ans.append(10**(d)+1)
for i in ans:
    print(i)