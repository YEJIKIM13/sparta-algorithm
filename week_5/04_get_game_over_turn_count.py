k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]


def get_d_index_when_go_back(d):
    if d % 2 == 0:  # 짝수라면
        return d + 1
    else:
        return d - 1

# 말은 순서대로 이동합니다 -> 말의 순서에 따라 반복문을 실행하겠구나!
# 말이 쌓일 수 있습니다 -> 맵에 말이 쌓이는 걸 저장해놔야 된다. (정보!)
# 쌓인 순서대로 이동합니다 -> (쌓인 걸 저장하는 자료구조인) stack 자료구조를 써야겠구나!
# 현재 맵에 어떻게 말이 쌓일지 저장하기 위해서는


# chess_map 과 동일하게 만들되 (이렇게 이차원 배열로 만들되)
# 안에는 링크드 리스트 즉, 리스트를 만들어 주면 될 것 같다.
def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(game_map)
    turn_count = 1  # 초기화, 우리가 원하는 게 이 게임이 몇 번이나 턴을 실행했는지이기 때문에 이 턴을 기준으로 반복을 하게 됨.
    # 안에 있는 배열은 n번 반복하고 있다.
    """
    current_stacked_horse_map = [
        [
            [] for _ in range(n)  # 각 원소에 배열을 넣어놔야지 링크드 리스트처럼 이렇게 이어서 현재 쌓여져 있는 말을 이렇게 쌓아놓을 수 있으니까!
        ] for _ in range(n)  # -> [] 가 n번 반복돼서 큰 배열 안에 저장이 된다.
    ]
    """
    # 배열이 n개 있고 그 배열이 n개 있는 삼차원 배열의 구성이구나 라고 생각!
    # 현재 체스 말들이 어떻게 쌓여있는지 저장하는 공간
    current_stacked_horse_map = [[[] for _ in range(n)] for _ in range(n)]
    # horse_location_and_directions 가 있어서 현재에 쌓여있는 말들의 배열도 current_stacked_horse_map 에 추가해보도록!
    for i in range(horse_count):  # 이거 반복문으로 써서 현재 horse 의 location 과 direction 을 여기다가 업데이트 시켜보자, 참고로 location 만 저장을 해 놓겠네
        r, c, d = horse_location_and_directions[i]
        current_stacked_horse_map[r][c].append(i)  # 위치만 저장할 것이기 떄문에 + append i 번째의 말이 현재 r, c의 위치에 있다라는 정보 저장

    # 이제 해야할 일: 각 말들을 규칙에 맞게 움직이기
    # 그 전에 이 프로그램은 게임이 종료되는 턴의 번호를 반환해야 함. 우리가 원하는 건 game_over_turn -> 변수로 해서 저장해 둠!
    while turn_count <= 1000:
        # 모든 각 말들을 돌아보면서 얘네가 방향에 맞게 움직이도록 해보자
        # 말들을 반복하기 위한 반복문
        for horse_index in range(horse_count):
            # horse_location_and_directions 에서 각 말들의 현재 위치와 방향을 알 수 있음, r, c, d 꺼내주기
            r, c, d = horse_location_and_directions[horse_index]
            # 방향으로 한 칸 이동했을 때 새로운 위치 알기 -> direction 변화량을 저장해 놓는 dr 과 dc 를 만들었었음! 마찬가지로 이것도 만들어주면 됨
            # 매 위치가 변경되는 것을 구했음
            new_r = r + dr[d]
            new_c = c + dc[d]

            # 파란색 칸 규칙
            # 만약 새로 이동할 것이 그 범위 안에 안 들어오거나 또는 그 위치가 파란색이다 (이동할 것의 game_map 이 2인 경우)
            # 그럼 반대로 한 칸을 이동하기로 함 == (0->1, 1->0, 2->3, 3->2) 이므로 홀수의 경우 -1 하고 짝수의 경우 +1 해주기 (get_d_index_when_go_back 함수 만들러 위로 가자!)
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d)

                # 방향을 옮겼으니 horse_location_and_directions 에서 업데이트를 다시 해줘야 함
                horse_location_and_directions[horse_index][2] = new_d  # 0 1 2 가 r c d 순이니까
                new_r = r + dr[new_d]
                new_c = c + dc[new_d]

                # 방향을 뒤집어서 갈 곳도 파란색이거나 막혀있다면? 이동 X
                # 가기로한 곳이 막혀있으면 안 감
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue  # 뒤집어서 갈 곳도 파란색이면 아무것도 안함

            # 이동할 애들 바리바리 가져오기!
            # 새로운 위치로 이동하기 전에 규칙이 있었음 == 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다... (pdf)
            # 지금같이 이동할 말을 저장하기 위해서는 현재 어떻게 쌓여져 있는지를 알아야 한다 -> current_stacked_horse_map
            # 근데 현재 이동할 애들이 기존의 위치에서 같이 있었던 애들이 여기 r, c에 존재할테니 이 친구들 하나하나 꺼내보자 (반복문 이용해 꺼내기)
            moving_horse_index_array = []
            for i in range(len(current_stacked_horse_map[r][c])):  # 인덱스 이용 위해 len()
                # 그치만 모든 애들을 꺼내가는 건 아니다!
                # 자기 자신의 인덱스보다 큰 애들만 데리고 감.
                # 여기서 i 번째는 [[[]]] 배열에 들어가있는 쌓여져 있는 말의 인덱스 번호이다. 이걸 변수로 current_stacked_horse_index 라고 하자
                current_stacked_horse_index = current_stacked_horse_map[r][c][i]
                if horse_index == current_stacked_horse_index:  # 현재 이동하고 있는 애(horse_index)와 같다면 current_ 이 녀석을 기준으로 이동을 시켜줘야 함!!
                    # 이동을 하는 애들을 저장하기 위해서 moving_horse_index_array 라는 변수를 둬야. 넣어줄 것의 인덱스부터의 애들을 지정한 것
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:]
                    # 여기까지가 이동할 것들이 타 있는 상태!
                    # 이동할 거니까 이 친구들을 current_stacked_horse_map 에 업데이트 시켜줘야 함. (인덱스 잘라서 남은 것 업데이트)
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i]

                    # 이렇게 이동을 하게 되면 반복을 안해도 됨, 이걸 했던 이유는 현재ㅐ 이동하려는 애가 뭐냐를 알고 싶어서 했던 것이기 때문.
                    break

            # 빨간색 칸
            # game_map 에 지금 이동하려는 칸 그리고 이동하려는 칸의 갑이 1이라는 배열을 뒤집어 버려야 했음
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)  # 뒤집은 후 넣어주러 가면 됨!

            # moving_horse_index_array 를 반복하면서 새롭게 이동할 current_stacked_horse_map 에 이동한 친구들을 쌓아주면 된다!
            for moving_horse_index in moving_horse_index_array:
                # 새로운 이동한 곳에 가서 업데이트를 해주는 것이기 때문에 new 에서 처리해야.
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)

                # 여기서 해야할 일: 현재 이동하는 말의 배열(moving_horse_index_array), 현재 쌓아져 있는 말들(current_stacked_horse_map)을 지도로 표시하고 있었는데
                # 다른 변수들도 있었음. horse_location_and_directions -> 현재 말들의 순서대로 어느 위치에 있고 어느 방향을 보고 있는지 저장해놓은 것이라서 말이 이동했으면 ** 업데이트 필수 **
                # 방금 옮긴 애의 행 열 값을 업데이트 해 줘야 함
                # 0번째 원소는 row(행) 값 저장, 첫 번째 값에는 열 값 저장. 거기다가 이동하는 new_r, new_c 값을 넣어 주면 됨!
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c

            # 파란색 칸 규칙 -> 맨 앞에 추가하는 게 가장 좋음
            # 왜냐면 moving_horse_index_array 를 쌓는 것들은 이 작업을 굳이 하지 않고 먼저 조건을 비교하는 게 더 빠르고 좋다!

            # 게임 끝나는 조건
            # 턴이 진행되는 중 말이 4개 이상 쌓이는 순간.
            # 다 이동시킨 이후에 새롭게 들어간 것의 개수가 4보다 크면 게임이 끝, turn_count 반환
            if len(current_stacked_horse_map[new_r][new_c]) >= 4:
                return turn_count

        # 반복을 할 때마다 turn_count 를 하나씩 늘려줘야지 원하는 결과 볼 수 있음
        turn_count += 1

    # while 문이 끝났는데도 아무것도 안됐으면 -1을 반환
    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다
