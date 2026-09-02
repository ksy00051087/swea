import sys
sys.stdin = open('input.txt', 'r')

"""
[SWEA] 단어 퍼즐 - 길이가 '정확히 K'인 단어가 들어갈 자리의 개수  (함수 없는 버전)

핵심 : "정확히 K" 의 의미
------------------------
K=3 인데 흰 칸이 4개 연속(1 1 1 1)이면 답은 0곳이다. 1곳도 2곳도 아니다.
한 자리(entry)는 검은 칸이나 격자 끝 사이에 끼인 '덩어리 전체'를 말하기 때문이다.
=> 우리가 셀 것은 "연속된 1 덩어리의 길이가 == K"인 덩어리 (>= K 가 아니다!)

함수를 안 쓰는 대신, 가로줄 N개와 세로줄 N개를 lines 라는 한 리스트에 미리 모아두고
그 리스트를 한 번만 훑는다. (같은 로직을 두 번 복붙하지 않는 요령)
"""

import sys
# sys.stdin = open('input.txt', 'r')   # 로컬 테스트용. 제출 시 주석 처리!
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # ── 검사 대상 2N개 줄을 한 리스트에 모은다 ──
    lines = []

    for r in range(N):                                  # 가로줄: 행을 그대로
        lines.append(board[r])

    for c in range(N):                                  # 세로줄: c 고정, r을 움직여 뽑음
        column = []
        for r in range(N):
            column.append(board[r][c])
        lines.append(column)
        # 위 4줄은 zip(*board) 한 방으로도 가능 (전치)

    # ── 각 줄에서 '길이가 정확히 K인 1 덩어리' 세기 ──
    answer = 0
    for line in lines:
        cnt = 0                       # 지금 이어지고 있는 1의 개수
        for v in line:
            if v == 1:
                cnt += 1              # 덩어리가 계속 이어짐
            else:
                if cnt == K:          # 0을 만났다 = 덩어리가 여기서 끝났다
                    answer += 1
                cnt = 0               # 다음 덩어리를 위해 리셋

        # ★ 줄이 1로 끝난 경우 for문 안에서는 검사할 기회가 없었다.
        #   반드시 반복문 밖에서 한 번 더 확인해야 한다.
        if cnt == K:
            answer += 1

    print(f'#{tc} {answer}')

"""
[검증] 1번 케이스 (N=5, K=3)
    0 0 1 1 1   → [111] 길이3 ✔
    1 1 1 1 0   → [1111] 길이4 ✘
    0 0 1 0 0   → 길이1 ✘
    0 1 1 1 1   → 길이4 ✘
    1 1 1 0 1   → [111] 길이3 ✔ , 길이1 ✘
    가로 2 + 세로 0 = 2  →  #1 2 ✅

[자주 하는 실수]
1) cnt >= K 로 검사 → 길이 5짜리 덩어리까지 세버림. 반드시 == K
2) 반복문이 끝난 뒤 마지막 검사를 빼먹음 → 줄 끝이 1로 끝나는 덩어리를 놓침
   (위 예제 첫 행이 정확히 그 경우라 예제부터 틀린다)
3) 세로에서 board[c][r] 로 인덱스를 뒤집음 → c번째 열은 board[r][c]에서 r을 움직인다
4) 가로만 세고 세로를 빼먹음 → 1번 케이스는 세로가 0이라 우연히 통과해서 더 위험

[더 짧게] 문자열로 바꿔 split 하면 줄 끝 처리가 저절로 된다.
    s = ''.join(map(str, line))                 # 예: "00111"
    answer += sum(1 for p in s.split('0') if len(p) == K)
"""