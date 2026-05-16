for T in range(1,int(input())+1):
    m = [list(input().split()) for i in range(4)]

    k = set()

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    def dfs(n,c,y,x):

        if n == 6:
            k.add(c)
            return
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 4 and 0 <= nx < 4:
                dfs(n + 1, c + m[ny][nx],ny,nx)

    for i in range(4):
        for j in range(4):
            dfs(0,m[i][j],i,j)
    
    print(f'#{T} {k}')