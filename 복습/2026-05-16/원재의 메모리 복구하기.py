# 직접 만든 코드
for T in range(1,int(input())+1):
    number = list(map(int,input()))

    ans = -1
    num = [0] * len(number)

    v = True
    ck = 0
    while True:
        ans += 1

        for i in range(len(number)):
            if number[i] != num[i]:
                ck = i
                a = number[i]
                break
                

        for i in range(len(num)-1,ck-1,-1):
            if num == number:
                v = False
                break
            num[i] = a
        
        if not v:
            break
            
    print(f'#{T} {ans}')

# ai 형태

for T in range(1,int(input())+1):
    number = list(input())

    c = '0'
    ans = 0
    for bit in number:
        if bit != c:
            ans += 1
            c = bit
            
    print(f'#{T} {ans}')