# 내 방법
for T in range(1,11):
    N = int(input())
    m = [list(input()) for i in range(8)]

    ans = 0
    for i in range(8):
        for j in range(8):
            try:
                k = j+N-1
                
                r1 = m[i][j:j+N]
                r2 = []
                
                for K in range(N):
                    r2.append(m[i][k-K])
                
                if r1 == r2:
                    ans += 1
            except:
                pass

    for i in range(8):
        for j in range(8):
            try:
                k = i+N-1
                
                r1 = []
                for K in range(N):
                    r1.append(m[i+K][j])

                r2 = []
                for K in range(N):
                    r2.append(m[k-K][j])

                if r1 == r2:
                    ans += 1
            except:
                pass

    print(f'#{T} {ans}')

# ai 방법
for T in range(1,11):
    
    N = int(input())
    m1 = [list(input()) for _ in range(8)]
    m2 = list(map(list, zip(*m1)))

    ans = 0
    for i in range(8):
        for j in range(8 - N + 1):
            r1 = m1[i][j:j+N]
            r2 = m2[i][j:j+N]

            if r1 == r1[::-1]: ans += 1
            if r2 == r2[::-1]: ans += 1

    print(f'#{T} {ans}')