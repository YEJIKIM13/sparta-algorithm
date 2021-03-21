from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 직관적으로 규칙성을 찾기가 쉽지 않음. 잘 안 보일 것 같아. -> BFS
# 방문 저장 여부 visited 를 만들어야 하는데
# 공이 2개? 어떻게 해야 방문하는지 아닌지를 알 수 있을까?
# 4차원 배열 사용! visited[red_marble_row][red_marble_col][blue_marble_row][blue_marble_col]
# 공간 낭비라고 생각할 수 있지만 보드의 행과 열의 길이가 고작 3 <= x <= 10 이라 괜찮


# 현재 row, 현재 col, 이동할 row, 이동할 col, game_map
def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):  # 게임 맵도 받아야 game_map 에서 이게 벽인지 구멍인지 알아야!
    move_count = 0
    # 언제까지 이동할 거냐면 벽이 아닐 때까지
    # 현재 있는 곳이 구멍이 아닐 때까지
    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "O":
        r += diff_r
        c += diff_c
        move_count += 1

    # 이동한 끝까지 간 위치 반환
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    n, m = len(game_map), len(game_map[0])  # 행과 열의 크기가 나옴
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # 4차원 배열로 visited 초기화 n m n m
    queue = deque()
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j

    # 탐색을 10번까지만 할 수 있다는 조건 -> 따라서 큐에 현재 탐색하는 숫자도 넣어줘야!
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True  # 조회했다고 할 수 있으니. 탐색할 준비 완료!

    # 큐를 이용해 탐색
    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        # 이제 네 방향에 대해서 어떻게 이동할건지 모든 경우를 시도
        for i in range(4): # 네 방향이니까 4번
            # 참고로 이 경우도 방향인데 방향이 끝까지 이동하는 거라서 그냥 한 칸 한 칸 이동이랑은 좀 다름..
            next_red_row, next_red_col, red_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)  # 함수, 현재 있는 위치를 가지고 현재 어느 방향을 볼 에정인지 넣자 -> i에 의해 결정
            next_blue_row, next_blue_col, blue_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            # 만약 블루가 먼저 구멍에 들어갔다면 게임이 끝났음. 망했어
            if game_map[next_blue_row][next_blue_col] == 'O':
                continue
            if game_map[next_red_row][next_red_col] == 'O':
                return True
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_count > blue_count:  # 이동한 횟수가 많은 애가 한 칸 떨어져야 한다
                    next_red_row -= dr[i]  # 아까 움직이기로 했던 만큼을 하나 더 띄어줌, 벽으로부터 한 칸 더 떨어지게
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:  # 방문하지 않았다 한다면
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col] = True  # 지금 방문하는 거니까 방문처리
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))  # 값을 큐에 추가 -> BFS 구현

    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
