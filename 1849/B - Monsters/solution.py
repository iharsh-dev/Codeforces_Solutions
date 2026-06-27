t = int(input())
for _ in range(t):
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    mapa={}
    arr=[]
    for i in range(n):
        if a[i]%k==0:
            mapa[i+1]=k
        else:
            mapa[i+1]=a[i]%k
    mapa_sorted = sorted(mapa, key=lambda x: mapa[x],reverse=True)
    print(*mapa_sorted)