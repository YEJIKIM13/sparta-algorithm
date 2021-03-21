from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
# 직관적으로 규칙성을 찾기가 쉽지 않음. 잘 안 보일 것 같아. -> BFS
# 방문 저장 여부 visited 를 만들어야 하는데
# 공이 2개? 어떻게 해야 방문하는지 아닌지를 알 수 있을까?
# 4차원 배열 사용! visited[red_marble_row][red_marble_col][blue_marble_row][blue_marble_col]
# 공간 낭비라고 생각할 수 있지만 보드의 행과 열의 길이가 고작 3 <= x <= 10 이라 괜찮


def is_available_to_take_out_only_red_marble(game_map):
    # 구현해보세요!
    n, m = len(game_map), len(game_map[0])  # 행과 열의 크기가 나옴
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # 4차원 배열로 visited 초기화 n m n m

    return


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
