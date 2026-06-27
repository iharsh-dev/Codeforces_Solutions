t = int(input())
 
for _ in range(t):
    n = int(input())
    s = input().strip()
 
    z = s.count('0')
 
    if z > 1 and z % 2 == 1 and s[n // 2] == '0':
        print("ALICE")
    else:
        print("BOB")