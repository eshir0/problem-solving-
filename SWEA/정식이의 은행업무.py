for T in range(1,int(input())+1):
    e = list(input())
    r = list(input())

    a, b = [], []

    for i in range(len(e)):
        if e[i] == '0':
            k = e[i]
            e[i] = '1'
            a.append(int(''.join(e), 2))
        elif e[i] == '1':
            k = e[i]
            e[i] = '0'
            a.append(int(''.join(e), 2))
        e[i] = k
    
    for i in range(len(r)):
        if r[i] == '0':
            k = r[i]
            r[i] = '1'
            b.append(int(''.join(r),3))
            r[i] = '2'
            b.append(int(''.join(r),3))
        elif r[i] == '1':
            k = r[i]
            r[i] = '0'
            b.append(int(''.join(r),3))
            r[i] = '2'
            b.append(int(''.join(r),3))
        elif r[i] == '2':
            k = r[i]
            r[i] = '1'
            b.append(int(''.join(r),3))
            r[i] = '0'
            b.append(int(''.join(r),3))
        r[i] = k
    
    
    ans = list(set(a) & set(b))[0]
    
    print(f'#{T} {ans}')