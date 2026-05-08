for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for _ in range(N)]

    ans = 0
    v = []

    dy = [1,1,-1,-1]
    dx = [1,-1,-1,1]

    def bfs():

        for i in range(4):

            while q: