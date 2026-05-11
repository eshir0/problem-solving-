for T in range(1,int(input())+1):
    m = [list(map(int,input().split())) for i in range(9)]

    def ck(y,x):
        for i in range(9):
            if x != i:
                if m[y][x] == m[y][i]:
                    return False 
        
        for i in range(9):
            if y != i:
                if m[y][x] == m[i][x]:
                    return False
        
        ny = y//3*3
        nx = x//3*3

        for i in range(ny,ny+3):
            for j in range(nx,nx+3):
                if y != i and x != j:
                    if m[y][x] == m[i][j]:
                        return False

        return True
    
    ans = 0
    
    for i in range(9):
        for j in range(9):
            a = 0
            if ck(i,j):
                pass
            else:
                a = 1
                break
        if a == 1:
            ans = 1
            break

    if ans == 1:
        print(f'#{T} 0')
    else:
        print(f'#{T} 1')