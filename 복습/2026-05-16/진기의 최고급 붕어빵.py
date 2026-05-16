for T in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    p = list(map(int,input().split()))

    b = 0
    ans = "Possible"

    for i in range(max(p)+1):
        if i == 0:
            pass
        elif i%M == 0:
            b += K

        if i in p:
            if b:
                b -= 1
            else:
                ans = "Impossible"
                break

    print(f'#{T} {ans}')