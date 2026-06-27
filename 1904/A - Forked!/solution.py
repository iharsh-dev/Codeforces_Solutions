t = int(input())
ans=[]
for _ in range(t):
    a, b = map(int,input().split())
    x_k, y_k = map(int,input().split())
    x_q, y_q = map(int,input().split())
    s = set()
    s = { (a,b), (a,-b), (-a,b), (-a,-b), (b,a), (b,-a), (-b,a), (-b,-a)}
    king = set(( ( x_k + dx ), ( y_k + dy ) ) for dx, dy in s )
    queen= set(( ( x_q + dx ), ( y_q + dy ) ) for dx, dy in s )
    ans.append(len(king&queen))
for i in ans:
    print(i)