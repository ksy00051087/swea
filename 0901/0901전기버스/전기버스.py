import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')
#현재 위치에서 갈수있는 위치에 충전소가 있는지 확인
# 없으면 뒤로 되돌아 가면서 충전하기
T = int(input())
for tc in range(1, T+1):
    #k는 충전량, N은 정류장 개수, M은 충전기 개수
    K, N, M = map(int, (input().split()))
    volt = list(map(int, input().split()))
    spot = [0] * (N+1)
    for i in range(M):
        spot[volt[i]] = 1
    #현재 위치에서 갈 수있는 정류장부터 충전기가 있는지 검사
    #없으면 되돌아가기
    # 충전기가 있으면 충전하기 >> 반복
    pos = 0 #현재위치
    cut = 0 # 충전 횟수 세기 변수
    while pos + K < N: # 충전기 찾아서 충전하기 반복
        # 갈수있는데 까지 가서 되돌아 오면서 찾기
        is_find = False
        for next in range(pos + K, pos, -1):
            if spot[next] == 1:# 충전기가 있는지
                cut += 1 # 충전하고 다음 충전소 찾기
                pos = next
                is_find = True
                break #  돌아가면서 찾기 중단
        # 충전소 찾는 반복문에서 충전소 찾았는가 확인
        if is_find == False:
            cut = 0
            break
    print(f"#{tc} {cut}")