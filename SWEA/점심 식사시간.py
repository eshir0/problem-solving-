for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    people = []
    stairs = []

    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                people.append((i,j))
            elif m[i][j] > 1:
                stairs.append((i, j, m[i][j]))
                
    ans = 1e9

    def time(g,si):
        if not g:
            return 0
        
        sy, sx, k = stairs[si]

        times = []
        for y, x in g:
            times.append(abs(y - sy) + abs(x - sx))
        times.sort()

        e_time = []
        
        for i in range(len(times)):
            arrival = times[i]

            if i < 3:
                start_d = arrival + 1
            
            else:
                start_d = max(e_time[i-3], arrival + 1)

            e_time.append(start_d + k)

        return e_time[-1]
    

    def dfs(n, A, B):
        global ans

        if n == len(people):

            time_A = time(A, 0)
            time_B = time(B, 1)
            
            cost = max(time_A,time_B)
            ans = min(ans,cost)
            return
        
        dfs(n + 1, A + [people[n]], B)
        dfs(n + 1, A, B + [people[n]])

    dfs(0,[],[])

    print(f'#{T} {ans}')