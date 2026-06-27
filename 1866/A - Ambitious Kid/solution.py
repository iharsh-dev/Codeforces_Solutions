n = int(input())
a = list(map(int, input().split()))
 
ans = min(abs(x) for x in a)
print(ans)