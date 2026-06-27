t = int(input())
ans = []
for _ in range(t) :
    w, h = map(int,input().split())
    arr = []
    for i in range(4):
        a = list(map(int,input().split()))
        arr.append(a)
    brr = [] 
    brr.append(abs(arr[0][1] - arr[0][-1])*h) 
    brr.append(abs(arr[1][1] - arr[1][-1])*h) 
    brr.append(abs(arr[2][1] - arr[2][-1])*w) 
    brr.append(abs(arr[3][1] - arr[3][-1])*w) 
    ans.append(max(brr))
for i in ans :
    print(i)