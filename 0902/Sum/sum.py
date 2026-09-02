import sys
sys.stdin = open('input.txt', 'r')

"""
[SWEA] 100x100 배열의 행/열/대각선 합 중 최댓값  (함수 없는 버전)

핵심
----
후보는 총 202개 : 행 100 + 열 100 + 대각선 2. 이 중 최댓값이 답.
    주대각선 ↘ : board[i][i]
    반대각선 ↙ : board[i][N-1-i]      (행+열 = N-1 이 항상 성립하므로 c = N-1-r)

★ 입력 형식이 진짜 함정이다
    - 맨 앞에 T(케이스 개수) 줄이 '없다'. 문제에 "총 10개"라고 못박혀 있다.
    - 대신 각 케이스의 첫 줄에 '테스트 케이스 번호'가 온다. 읽어서 버려야 한다.
    습관적으로 T = int(input()) 를 쓰면 첫 케이스 번호 "1"을 T로 먹어버려
    케이스 하나만 처리하고 끝난다.
"""


N = 100   # 배열 크기가 문제에서 고정
T = 10    # 테스트 케이스 개수도 고정 (입력에 없다)

for tc in range(1, T + 1):
    input()                                                       # ★ 케이스 번호 줄 버리기
    board = [list(map(int, input().split())) for _ in range(N)]

    best = 0

    # ── 각 행의 합 ──
    for r in range(N):
        s = sum(board[r])          # 행은 리스트 그 자체라 sum()을 바로 쓸 수 있다
        if s > best:
            best = s

    # ── 각 열의 합 ──
    for c in range(N):
        s = 0
        for r in range(N):         # c 고정, r을 움직인다
            s += board[r][c]
        if s > best:
            best = s

    # ── 주대각선 ↘ ──
    s = 0
    for i in range(N):
        s += board[i][i]
    if s > best:
        best = s

    # ── 반대각선 ↙ ──
    s = 0
    for i in range(N):
        s += board[i][N - 1 - i]
    if s > best:
        best = s

    print(f'#{tc} {best}')

"""
[검증] 문제 그림의 5x5 예시
    4 4 3 2 1      행 합    : 14 16 25 27 29
    2 2 1 6 5      열 합    : 21 14 22 28 26
    3 5 4 6 7      주대각선 : 4+2+4+9+6 = 25
    4 2 5 9 7      반대각선 : 1+6+4+2+8 = 21
    8 1 9 5 6      최댓값 = 29 ✅

[자주 하는 실수]
1) ★ 케이스 번호 줄을 안 버림 → 두 번째 케이스부터 입력이 밀려 전부 틀림 (실패 원인 1위)
2) T = int(input()) 을 습관적으로 씀 → 이 문제 입력엔 T 줄이 없다
3) 반대각선을 board[N-1-i][i] 로 씀 → 같은 대각선을 거꾸로 훑는 것이라 합은 우연히 같지만,
   순서가 중요한 문제에서는 결과가 달라진다. r + c == N-1 로 이해해 둘 것
4) best = 0 초기화 → 값이 음수일 수 있는 문제라면 -float('inf')를 써야 한다

[더 짧게]
    rows = [sum(row) for row in board]
    cols = [sum(col) for col in zip(*board)]          # zip(*board) = 전치
    d1 = sum(board[i][i] for i in range(N))
    d2 = sum(board[i][N-1-i] for i in range(N))
    best = max(rows + cols + [d1, d2])
"""