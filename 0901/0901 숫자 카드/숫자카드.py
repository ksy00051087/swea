import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = input().strip()          # 여백 없이 붙어 있으므로 문자열 그대로 받는다
                                     # int로 받으면 "08271"의 앞 0이 날아감

    # 카운팅 정렬 아이디어: 값의 범위가 0~9로 고정 → 크기 10짜리 배열로 O(N) 집계
    cnt = [0] * 10
    for c in cards:
        cnt[int(c)] += 1

    # 동점 처리: 0→9 오름차순으로 훑으면서 >= 로 비교
    # >= 이므로 장수가 같으면 뒤에 나온(=더 큰) 숫자로 계속 갱신된다
    num = 0
    for d in range(10):
        if cnt[d] >= cnt[num]:
            num = d

    print(f"#{tc} {num} {cnt[num]}")

# 포인트는 두 가지입니다. 입력을 문자열로 받아야 앞자리 0이 보존된다는 점
# 그리고 동점일 때 큰 수를 고르는 조건을 > 대신 >=로 두고 오름차순으로 훑어 자연스럽게 해결한다는 점입니다.
# N은 사실 쓰지 않아도 되지만 입력 형식상 읽어야 합니다. 전체 복잡도는 O(N)입니다.