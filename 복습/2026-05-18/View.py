for T in range(1,11):
    N = int(input())
    m = list(map(int,input().split()))

    ans = 0

    for i in range(2,N-2):
        if m[i-1] < m[i] and m[i-2] < m[i] and m[i+1] < m[i] and m[i+2] < m[i]:
            a = max(m[i-2:i])
            b = max(m[i+1:i+3])
            cost = m[i] - max(a,b)
            ans += cost
    print(f'#{T} {ans}')