# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1. 시작 노드를 스택에 넣습니다.
# 2. 현재 스택의 노드를 빼서 visited 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중에서 방문하지 않은 노드를 스택에 추가합니다.


def dfs_stack(adjacent_graph, start_node):
    stack = [start_node]
    visited = []  # 방문한 걸 저장하기 위한 배열 정의

    # while 문을 사용해서 스택이 비지 않았다고 말하기!
    while stack:
        current_node = stack.pop()  # 현재 스택의 노드를 빼서 current_node 라는 변수에 담자
        visited.append(current_node)  # visited 배열에 current_node 를 붙임
        # 그럼 지금 start-node 가 1이니까 visited 는 1이 됨!! (처음)  [1]
        for adjacent_node in adjacent_graph[current_node]:  # 인접한 노드 꺼내기, current_node 의 adjacent_graph 에 인접한 노드들을 보고 싶은 거니까
            if adjacent_node not in visited:  # visited 배열에 없다면 방문하지 않은 거니까 이 녀석 스택에 추가해주기
                stack.append(adjacent_node)

    return visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!
