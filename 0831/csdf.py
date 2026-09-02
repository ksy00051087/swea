import sys
sys.stdin = open("input.txt", "r")

T = 10

for tc in range(1, T+1):
    N = int(input())
    apt = list(map(int, input().split()))
    # 각 건물의 조망권이 확보된 세대수 합 구하기
    sum_v = 0
    #각 건물의 조만권 계산하기
    for i in range(2, N-2):
        # i : 건물 번호
        # i번 건물의 양쪽 2칸 보기 i-2 ~ i+2번까지 (i는 제외)
        # 건물 네개 중에 제일 노ㅠ은 건물 높이 찾기
        max_height = 0
        for j in range(i-2, i+3):
            if j == i: continue #현재 건물은 비교대상에 제외
            if apt[j] > max_height:
                max_height = apt[j]
        # 현재건물 (apt[i]가 주변 건물보다 높을 떄만
        if apt[i] > max_height:
            sum_v = sum_v + (apt[i] - max_height)
    print(f'#{tc} {sum_v}')