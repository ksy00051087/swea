import sys
sys.stdin = open('input.txt', 'r')
T = 10
for tc in range(1, T + 1):                    # 테스트케이스 10개 고정
    dump = int(input())                    # 덤프 횟수
    box = list(map(int, input().split()))  # 높이 100칸

    for i in range(dump):
        box.sort()                         # box[0]=최저, box[-1]=최고
        # if box[-1] - box[0] <= 1:          # 이미 평탄 → 더 옮기면 오히려 벌어짐
        #     break # 이자식을 왜 넣으면 안되는지 모르겠다
        box[0] += 1
        box[-1] -= 1

    box.sort()                             # 루프 탈출 시 정렬이 깨져 있을 수 있음
    print(f"#{tc} {box[-1] - box[0]}")