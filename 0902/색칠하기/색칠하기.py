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

import sys
# sys.stdin = open('sample_input.txt', 'r')   # 로컬 테스트용. 제출 시 주석 처리!
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N = int(input())                       # 색칠 영역(직사각형) 개수

    # 10x10 격자를 0으로 초기화
    # [[0]*10]*10 은 같은 리스트를 10번 참조해서 버그가 남 → 반드시 컴프리헨션
    board = [[0] * 10 for _ in range(10)]

    # ── N개의 직사각형을 하나씩 칠한다 ──
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())

        # (r1,c1)부터 (r2,c2)까지 '끝 칸 포함' → range는 끝을 제외하므로 +1 필수
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                board[r][c] += color       # 빨강(1) 위에 파랑(2) → 3(보라)

    # ── 보라색(3) 칸 세기 ──
    count = 0
    for r in range(10):
        for c in range(10):
            if board[r][c] == 3:
                count += 1

    print(f'#{tc} {count}')

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