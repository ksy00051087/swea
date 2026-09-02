import sys
sys.stdin = open('input.txt', 'r')

"""
[SWEA] 부분집합의 합 - {1..12}의 부분집합 중 원소 N개, 합 K인 것의 개수  (함수 없는 버전)

핵심 : 비트마스크로 부분집합 전부 만들기
---------------------------------------
원소 12개 → 각 원소마다 "넣는다/뺀다" 2가지 → 부분집합 2^12 = 4096개.
이 4096개를 정수 0~4095 하나하나로 표현한다.

    code의 i번째 비트가 1  ==  숫자 (i+1)을 포함
    확인 방법 : code & (1 << i)  가 0이 아니면 켜져 있음

예) code = 13 = 1101(2) → 비트 0,2,3 → {1, 3, 4}
"""

import sys
# sys.stdin = open('sample_input.txt', 'r')   # 로컬 테스트용. 제출 시 주석 처리!
input = sys.stdin.readline

NUMS = list(range(1, 13))   # [1..12] — 문제에서 고정된 집합 (입력으로 안 들어온다)
SIZE = 12

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())    # N: 원소 개수, K: 원소 합

    count = 0

    # 0 ~ 2^12-1 = 모든 부분집합 (0은 공집합, 4095는 전체집합)
    for code in range(1 << SIZE):       # 1 << 12 == 4096
        cnt = 0      # 이 부분집합의 원소 개수
        total = 0    # 이 부분집합의 원소 합

        for i in range(SIZE):
            if code & (1 << i):        # i번째 비트가 켜져 있으면
                cnt += 1               #   NUMS[i]를 포함한다는 뜻
                total += NUMS[i]
                if total > K:          # 가지치기: 합이 이미 K를 넘음
                    break

        # 개수와 합, 두 조건을 '동시에' 만족해야 한다
        if cnt == N and total == K:
            count += 1

    print(f'#{tc} {count}')

"""
[검증]
    N=3, K=6  → {1,2,3} 하나         →  1 ✅
    N=5, K=15 → 원소 5개의 최소합이 1+2+3+4+5=15 이므로 {1,2,3,4,5} 하나  →  1 ✅
    N=5, K=10 → 최소합 15 > 10 이라 불가능  →  0 ✅

[자주 하는 실수]
1) 집합 A를 입력에서 읽으려 함 → A는 항상 {1..12} 고정, 입력은 N과 K뿐
2) cnt == N 검사를 빼먹고 합만 봄 → 답이 커짐
3) range(1 << SIZE)를 range(SIZE)로 착각 → 4096이 아니라 12번만 돎
4) count를 테스트 케이스 밖에서 초기화 → 답이 계속 누적됨

[다른 풀이] 원소 개수가 N개로 고정이므로 조합으로 바로 뽑는 게 더 빠르다.
    from itertools import combinations
    count = sum(1 for c in combinations(NUMS, N) if sum(c) == K)
"""