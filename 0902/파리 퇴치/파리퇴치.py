import sys
sys.stdin = open('input.txt', 'r')

"""
[SWEA] 파리 퇴치 - NxN 격자에서 MxM 파리채로 잡을 수 있는 최대 파리 수  (함수 없는 버전)

핵심
----
파리채는 격자를 벗어날 수 없으므로, 왼쪽 위 모서리 (i, j)만 정하면 위치가 결정된다.
    덮는 범위 : 행 i ~ i+M-1,  열 j ~ j+M-1
    벗어나지 않으려면 i+M-1 <= N-1  →  i <= N-M
    따라서 i, j 는 각각 0 ~ (N-M),  즉 range(N-M+1)
가능한 위치를 전부 놓아보고(완전 탐색) 합의 최댓값을 고른다.
"""

import sys
# sys.stdin = open('input.txt', 'r')   # 로컬 테스트용. 제출 시 주석 처리!
input = sys.stdin.readline

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())                              # N: 격자 크기, M: 파리채 크기
    board = [list(map(int, input().split())) for _ in range(N)]

    best = 0   # 파리 수는 0 이상이므로 0으로 시작해도 안전

    # ── 파리채 왼쪽 위 모서리를 모든 가능한 위치로 이동 ──
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            # 덮인 MxM 영역의 합
            total = 0
            for di in range(M):          # di: 파리채 안 행 오프셋
                for dj in range(M):      # dj: 파리채 안 열 오프셋
                    total += board[i + di][j + dj]

            if total > best:
                best = total             # best = max(best, total) 와 동일

    print(f'#{tc} {best}')

"""
[검증] 1번 케이스 (N=5, M=2)
    1  3  3  6  7
    8 13  9 12  8
    4 16 11 12  6
    2  4  1 23  2
    9 13  4  7  3
    (1,1) 위치 : 13+9+16+11 = 49  ← 최댓값  →  #1 49 ✅

[자주 하는 실수]
1) range(N-M) 처럼 +1을 빼먹음 → 오른쪽/아래 끝 위치를 놓쳐 답이 작아짐
2) best 초기화를 반복문 밖에 두어 이전 케이스 값이 남음
3) 파리채가 격자를 벗어나도 된다고 착각 → 탐색 범위 근거가 사라짐

[확장] N이 1000쯤 되면 O(N^2 * M^2)가 터진다. 그때는 2차원 누적합으로
어떤 직사각형 합도 뺄셈 3번(O(1))에 구해 O(N^2)로 줄인다.
    P[i][j] = board[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]
"""