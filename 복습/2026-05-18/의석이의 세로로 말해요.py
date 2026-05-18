for T in range(1,int(input())+1):
    m = [list(input()) for i in range(5)]
    
    max_ = 0
    for i in range(5):
        max_ = max(max_,len(m[i]))
    

    ans = ""
    for i in range(max_):
        for j in range(5):
            try:
                ans += m[j][i]
            except:
                pass

    print(f'#{T} {ans}')