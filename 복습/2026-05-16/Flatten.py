for T in range(1,11):
    N = int(input())
    num = list(map(int,input().split()))
    
    for i in range(N):
        for j in range(len(num)):
            if max(num) == num[j]:
                num[j] -= 1
                break

        for j in range(len(num)):
            if min(num) == num[j]:
                num[j] += 1
                break
    
    print(f'#{T} {max(num) - min(num)}')