for T in range(1,int(input())+1):
    N = int(input())

    v = [0] * N

    def ck(n):
        for i in range(n):
            if v[n] == v[i] or abs(v[n] - v[i]) == abs(n - i):
                return False
        return True


    ans = 0
    def dfs(n):
        global ans

        if n == N:
            ans += 1
            return
        
        for i in range(N):
            v[n] = i

            if ck(n):
                dfs(n+1) 
    
    dfs(0)
    print(f'#{T} {ans}')