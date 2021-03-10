# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
# 인접한 노드가 뭔지 나열이 되어있음
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
visited = []

# 1. 시작노드(루트노트)인 1부터 탐색합니다.
# 2. 현재 방문한 노드를 visited_array 에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드에 방문합니다.


# cur_node == 시작하는 노드
# visited_array == 바깥에 정의 되어 있는 빈 배열인 visited 전달해서 넘겨 줌
def dfs_recursion(adjacent_graph, cur_node, visited_array):
    # 일단 시작 노드를 visited_array 에 추가
    visited_array.append(cur_node)  # 2번 작업
    # 방문한 노드와 인접한 노드 중 방문하지 않은 노드 찾아야 함 -> adjacent_graph 통해 인접 노드 찾을 수 있음
    for adjacent_node in adjacent_graph[cur_node]:  # 그 노드를 봐야하니까! cur_node, 방문 여부는 visited_array 확인
        if adjacent_node not in visited_array:  # 방문한 적이 없다면 다시 dfs_recursion 함수 호출
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)


# 탈출 조건 안 써줘도 되나요?! ->
# adjacent_node 가 visited_array 에 있는지 없는지 검사하는 게 바로 탈출조건!


dfs_recursion(graph, 1, visited)  # 1 이 시작노드입니다!
print(visited)  # 모든 노드를 방문해야 하니까 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
