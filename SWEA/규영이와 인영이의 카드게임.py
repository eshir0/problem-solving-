# 직접 푼것 (ai가 따로 number를 구해야한다는 것만 알려줌)
for T in range(1,int(input())+1):
    number1 = list(map(int,input().split()))
    number2 = []
    for i in range(1,19):
        if i not in number1:
            number2.append(i)

    max_ = 0
    min_ = 0
    s = set()

    v = [False] * 9
    
    def dfs(n,a,b):
        global min_, max_

        if n == 9:
            if a > b:
                min_ += 1
            
            elif a < b:
                max_ += 1
            
            return
        
        for i in range(9):
            if not v[i]:
                v[i] = True
                if number1[n] < number2[i]:
                    b += number1[n] + number2[i]
                    dfs(n+1,a,b)
                    b -= number1[n] + number2[i]
                elif number1[n] > number2[i]:
                    a += number1[n] + number2[i]
                    dfs(n+1,a,b)
                    a -= number1[n] + number2[i]
                else:
                    dfs(n+1,a,b)
                v[i] = False

    dfs(0,0,0)
    print(f'#{T}',min_, max_)