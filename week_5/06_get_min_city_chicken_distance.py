import itertools, sys

n = 5
m = 3

city_map = [
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 1],
    [0, 1, 2, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 2],
]


# 여러 개 중에서 M개를 고른 뒤, 모든 치킨 거리의 합이 가장 작게 되는 경우를 반환
# -> 여러 개 중에서 특정 개수를 뽑는 경우의 수 / (모든 치킨 거리의 합을 전부 다 구해야 한다는 말)
# 이렇게 특정 개수를 뽑아야 하고 모든 경우의 수를 다 구해야 한다? -> 조합 사용

def get_min_city_chicken_distance(n, m, city_map):
    chicken_location_list = []  # 치킨집의 위치를 저장하기 위한 배열
    home_location_list = []
    for i in range(n):  # n은 city_map 의 행과 열의 길이
        for j in range(n):
            if city_map[i][j] == 1:
                home_location_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_location_list.append([i, j])

    # chicken_location_list 가지고 조합 만들어보기, 보기 좋게 리스트로 감싸고 변수에 저장
    chicken_location_m_combinations = list(itertools.combinations(chicken_location_list, m))
    # print(chicken_location_m_combinations) -> [([1, 2], [2, 2], [4, 4])] 이건 사실 튜플 하나만 담긴 것
    # 왜냐면 지금 입력값 치킨집이 3개라 조합이 하나밖에 없어서 한 개 밖에 안나옴!

    # 최소 도시 치킨 거리 구하기
    min_distance_of_m_combinations = sys.maxsize

    for chicken_location_m_combination in chicken_location_m_combinations:  # 조합을 꺼내올 것
        city_chicken_distance = 0  # 이 조합에서 얻고 싶은 건 도시 치킨거리가 얼마나 될지니까 초기화

        # 각 집들의 치킨 거리 알아내야 하니까 각 집의 위치 뽑아내기
        for home_r, home_c in home_location_list:
            min_home_chicken_distance = sys.maxsize
            # 이 값을 각 치킨집을 보면서 어디가 가까운지를 보고 뽑아보면 됨
            for chicken_location in chicken_location_m_combination:
                # 어느 경우에 chicken_distance 가 제일 작은지를 계산
                min_home_chicken_distance = min(
                    min_home_chicken_distance,  # 현재 min_home_chicken_distance 보다 작은가
                    # 혹은 지금 집에 있는 위치와 치킨집 위치의 절대값을 비교, chicken_location[0]에는 row 값, [1]에는 col 값
                    abs(home_r - chicken_location[0]) + abs(home_c - chicken_location[1])
                )

            # 도시의 최소 치킨거리 + 집의 치킨거리
            city_chicken_distance += min_home_chicken_distance

        # combinations 를 다시 한 번 city_chicken_distance 랑 비교해서 최솟값을 넣어주면 됨
        min_distance_of_m_combinations = min(min_distance_of_m_combinations, city_chicken_distance)

    return min_distance_of_m_combinations


# 출력
print(get_min_city_chicken_distance(n, m, city_map))  # 5 가 반환되어야 합니다!
