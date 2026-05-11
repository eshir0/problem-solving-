# 내가 푼거
for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    ans = [[] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ans[i].append(m[N-1-j][i])

        for j in range(N):
            ans[i].append(m[N-1-i][N-1-j])

        for j in range(N):
            ans[i].append(m[j][N-1-i])
	
    print(f'#{T}')
    for i in range(N):
        for j in range(0,len(ans[i]),N):
            a = ""
            for k in range(N):
                a += str(ans[i][j+k])
            print(''.join(a), end=" ")
        print()

# ai가 알려준 방법
for T in range(1, int(input()) + 1):
    N = int(input())
    m = [list(input().split()) for _ in range(N)]
    
    print(f'#{T}')
    for i in range(N):
        r90 = ''.join(m[N-1-j][i] for j in range(N))
        r180 = ''.join(m[N-1-i][N-1-j] for j in range(N))
        r270 = ''.join(m[j][N-1-i] for j in range(N))
        
        print(f'{r90} {r180} {r270}')