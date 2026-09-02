import sys
sys.stdin = open('input.txt', 'r')

"""
[SWEA] 스도쿠 검증 - 9x9가 스도쿠 규칙을 만족하면 1, 아니면 0  (함수 없는 버전)

핵심 : "중복 없음" == set으로 만들면 {1..9} 와 같다
--------------------------------------------------
    set([7,3,6,4,2,9,5,8,1]) == {1..9}  ✔
    set([8,9,2,1,2,5,6,7,4])            ← 2가 중복 → 원소 8개 ✘
검사 대상은 총 27개 그룹 : 행 9 + 열 9 + 3x3 박스 9.

함수가 없으면 return으로 즉시 빠져나갈 수 없다.
그래서 ok 라는 '플래그 변수'를 두고, 위반을 발견하면 False로 바꾼다.
(이게 함수를 쓰는 가장 큰 이유였다 — 없으면 이렇게 플래그로 대신한다)
"""

import sys
# sys.stdin = open('input.txt', 'r')   # 로컬 테스트용. 제출 시 주석 처리!
input = sys.stdin.readline

FULL = set(range(1, 10))   # {1,2,...,9}

T = int(input())

for tc in range(1, T + 1):
    # 이 문제는 크기(N) 줄이 없다. 곧바로 9줄이 퍼즐 데이터다.
    board = [list(map(int, input().split())) for _ in range(9)]

    ok = True   # 아직 위반을 못 찾았다는 뜻

    # ── (1) 가로줄 9개 ──
    for r in range(9):
        if set(board[r]) != FULL:
            ok = False

    # ── (2) 세로줄 9개 ──
    for c in range(9):
        column = []
        for r in range(9):          # c 고정, r을 움직인다
            column.append(board[r][c])
        if set(column) != FULL:
            ok = False

    # ── (3) 3x3 박스 9개 ──
    # 박스의 시작 좌표는 0, 3, 6 → range(0, 9, 3)  (range(3)이 아니다!)
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            box = []
            for dr in range(3):
                for dc in range(3):
                    box.append(board[br + dr][bc + dc])
            if set(box) != FULL:
                ok = False

    print(f'#{tc} {1 if ok else 0}')

"""
[검증] 2번 케이스가 이 문제의 백미
    9개 '행'은 전부 정상이다. 그런데 열을 세워보면
        열3 : 4 7 5 2 1 9 3 6 1   ← 1이 두 번
        열4 : 8 3 6 5 8 4 2 7 9   ← 8이 두 번
    행만 검사한 코드는 이걸 1로 잘못 출력한다.
    → 행/열/박스 세 조건이 서로 독립임을 데이터로 증명해 주는 케이스.

    7번 케이스는 눈으로도 보인다 : 8 9 2 1 2 5 6 7 4  (2가 두 번)

[자주 하는 실수]
1) 크기(N) 줄을 읽으려고 input()을 한 번 더 호출 → 이 문제엔 그 줄이 없다.
   한 줄만 잘못 소비해도 이후 케이스가 전부 밀린다.
2) 행만 검사하고 끝냄 → 2번 케이스에서 바로 걸린다
3) 박스 순회를 range(3)으로 씀 → 시작 좌표는 0,3,6 이므로 range(0,9,3)
4) 위반을 찾은 뒤 ok를 다시 True로 덮어씀 → ok는 한 번 False가 되면 끝까지 False여야 한다

[성능 메모] 함수 버전은 위반을 찾는 즉시 return 0 으로 빠져나가지만
이 버전은 27개 그룹을 끝까지 다 본다. 27x9=243번뿐이라 체감 차이는 없다.
빠져나가고 싶다면 각 반복문에 break를 걸고 바깥에서 if not ok: break 를 추가하면 된다.
"""