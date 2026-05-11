# 맵을 돌려 교착 상태 확인
for _ in range(1,11):
    N = int(input())
    m = [list(map(int,input().split())) for I in range(100)]

    row = list(map(list, zip(*m)))
    total = 0

    for r in row:
        flag = False

        for i in r:
            if i ==1:
                flag = True
            elif i == 2:
                if flag:
                    total += 1
                    flag = False
                    
    print(f"#{_} {total}")

# 직접 만든 일반적인 버전
for t in range(1,11):
    a = int(input())
    m = [list(map(int,input().split())) for _ in range(a)]

    ans = 0

    def ck(y,x):

        for i in range(y+1,a):
            if m[i][x] == 1:
                return 0
            elif m[i][x] == 2:
                return 1
        return 0

    for i in range(a):
        for j in range(a):
            if m[j][i] == 1:
                ans += ck(j,i)

    print(f'#{t} {ans}')