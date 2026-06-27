t = int(input())
ans = [] 
for _ in range(t):
    a = input()
    b = input()
    if len(a) <= len(b):
        sm = a 
        bi = b 
    else:
        sm = b 
        bi = a 
    maxx = 0
    arr =0
    check = False
    for i in range(len(sm)):
        for j in range(len(bi)):
            if sm[i] == bi[j]:
                count = 0
                k = i
                l = j
                while k<len(sm) and l<len(bi) and sm[k]==bi[l]:
                    count+=1
                    k+=1
                    l+=1 
                if count > maxx:
                    check = True
                    maxx = count
                    arr = i+j+len(sm)-k+len(bi)-l
    if check:
        ans.append(arr)
    else:
        ans.append(len(sm)+len(bi))
for i in ans:
    print(i)