import sys
sys.stdin = open('input.txt', 'r')

"""
[SWEA] 색칠하기 - 10x10 격자에서 빨강+파랑이 겹친 보라색 칸 수 세기  (함수 없는 버전)

핵심
----
칸마다 상태를 숫자 하나로 저장한다.
    0=아무것도 안 칠함, 1=빨강만, 2=파랑만, 3=빨강+파랑(보라)
3 = 1 + 2 이므로, "같은 색끼리는 겹치지 않는다"는 문제 조건 덕분에
board[r][c] += color 로 그냥 누적해도 값이 절대 꼬이지 않는다.
"""


T = int(input())

for tc in range(1, T + 1):
    N = int(input())                      
    board = [[0] * 10 for _ in range(10)]  # 10x10 격자판 초기화

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1 - 1, r2):  # 행 범위
            for c in range(c1 - 1, c2):  # 열 범위
                board[r][c] += color

    # 보라색 칸 수 세기
    cnt = 0         



    for r in range(10): 
            
        for c in range(10): 
            if board[r][c] == 3:  # 빨강+파랑
                cnt += 1    


    print(f'#{tc} {cnt}')
"""
[검증] 1번 케이스
    2 2 4 4 1  → 행2~4, 열2~4 빨강
    3 3 6 6 2  → 행3~6, 열3~6 파랑
    겹침 = 행[3,4] x 열[3,4] = 2x2 = 4  →  #1 4 ✅

[자주 하는 실수]
1) range(r2) 처럼 +1을 빼먹음 → 오른쪽/아래 한 줄이 통째로 누락
2) board를 테스트 케이스마다 초기화하지 않음 → 이전 색이 남아 답이 커짐
3) [[0]*10]*10 사용 → 한 행을 바꾸면 전 행이 같이 바뀌는 참조 버그
"""