for T in range(1,int(input())+1):
    num, N = input().split()
    N = int(N)
    num = list(num)

    v = set()

    ans = 0
    def dfs(n):
        global ans

        if n == N:
            number = ''.join(num)
            ans = max(ans,int(number))
            return
        
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                num[i],num[j] = num[j],num[i]

                number = ''.join(num)

                if (number, n + 1) not in v:
                    v.add((number, n + 1))   
                    dfs(n+1)

                num[i],num[j] = num[j],num[i]
    
    dfs(0)
    print(f'#{T} {ans}')