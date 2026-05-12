# N : 손님 수 , M : 초 , K : M 후 만들어지는 붕어빵 개수

for T in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    number = list(sorted(map(int,input().split())))

    ans = "Possible"

    for i in range(N):
        
        m = (number[i] // M) * K

        if m < (i + 1):
            ans = "Impossible"
            break

    print(f'#{T} {ans}')