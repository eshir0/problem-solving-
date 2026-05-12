#include <stdio.h>
#include <stdbool.h>

int number1[9]; // 1번 플레이어의 카드
int number2[9]; // 2번 플레이어의 카드
bool v[9];      // 2번 플레이어 카드 사용 여부 (방문 배열)
int min_ = 0;   // 1번 플레이어 승리 횟수 (a > b)
int max_ = 0;   // 2번 플레이어 승리 횟수 (a < b)

// n: 진행된 라운드 수, a: 1번 플레이어 점수, b: 2번 플레이어 점수
void dfs(int n, int a, int b){
    // 9라운드가 모두 끝난 경우 승패 판별
    if (n == 9){
        if (a > b){
            min_++;
        } else if (a < b){
            max_++;
        }
        return;
    }

    // 2번 플레이어가 낼 수 있는 9장의 카드 중 하나를 선택 (순열 탐색)
    for (int i = 0; i < 9; i++){
        if (!v[i]){
            v[i] = true; // 카드 사용 처리

            // 카드 대소 비교에 따라 이긴 사람에게 점수(두 카드의 합) 부여 후 다음 라운드 진행
            if (number1[n] < number2[i]){
                dfs(n + 1, a, b + number1[n] + number2[i]);
            } else if (number1[n] > number2[i]){
                dfs(n + 1, a + number1[n] + number2[i], b);
            } else {
                dfs(n + 1, a, b); // 비긴 경우 점수 변동 없음
            }

            v[i] = false; // 다른 경우의 수 탐색을 위해 카드 사용 상태 원상복구(백트래킹)
        }
    }
}

int main() {
    int T;

    // 테스트 케이스 개수 입력
    if (scanf("%d", &T) != 1) return 0;

    for (int t = 1; t <= T; t++){
        bool cards[19] = {false}; // 1~18번 카드 중 1번 플레이어 소유 여부 체크

        // 1번 플레이어의 카드 9장 입력
        for (int i = 0; i < 9; i++){
            scanf("%d", &number1[i]);
            cards[number1[i]] = true; // 입력받은 카드는 true로 체크
        }

        // 1번 플레이어가 갖지 않은 나머지 9장(false)을 2번 플레이어 배열에 할당
        int idx = 0;
        for ( int i = 1; i <= 18; i++) {
            if (!cards[i]){
                number2[idx++] = i;
            }
        }

        // 새로운 테스트 케이스 시작 전 전역 변수 초기화
        min_ = 0;
        max_ = 0;
        for (int i = 0; i < 9; i++){
            v[i] = false;
        }

        // 0라운드, 양측 점수 0점으로 DFS 시작
        dfs(0, 0, 0);
        
        // 결과 출력
        printf("#%d %d %d\n", t, min_, max_);
    }
    return 0;
}