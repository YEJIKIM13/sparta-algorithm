genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 헷갈리면 중간 중간 출력해서 결과값 확인할 것!
# 속한 노래가 가장 많이 재생된 장르를 보는 순간 -> 장르별로 노래를 순서대로 정렬해야겠다 라고 생각!
# 장르 별로(key) 우선 재생된 횟수(value)를 저장해야 한다!
# 장르 별로 곡의 정보 (인덱스, 재생횟수) 배열로 묶어 저장한다!


def get_melon_best_album(genre_array, play_array):
    genre_total_play_dict = {}
    genre_index_play_array_dict = {}  # 장르별로 인덱스와 플레이를 담은 배열을 딕셔너리 형태로 저장한다.
    # 장르의 길이를 변수에 저장
    n = len(genre_array)
    # 반복을 통해서 장르와 플레이 수를 해당 딕셔너리에 담기
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        # 얘네를 장르 토탈 플레이 딕셔너리에 추가해주면 됨
        # for 문 안에서!!!
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play  # 초기값 설정 필수
            genre_index_play_array_dict[genre] = [[i, play]]  # 장르 값으 배열로 만들겠다! 장르 별로 여러 곡이 쌓일 거니까.
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    # 장르 내에서도 많이 재생된 노래를 비교를 해서 먼저 수록을 해줘야 함
    # 장르 별로 플레이 수가 몇인지 저장을 해놔야 함 (재생된 노래가 뭔지도 알아야 하기 때문에 인덱스도 저장)
    # 재생된 수가 많은 장르부터 재생된 수가 많은 곡을 수록하면 됨 -> 많이 재생된 장르 알아야
    # 딕셔너리 어떻게 정렬? -> 딕셔너리.items() 를 사용하면 됨 -> dict_items 라는 곳에 배열이 달려서 온다. 배열 안에는 키, 값이 담긴 튜플이 배열로 감싸져서 나옴
    # dict_items([('classic', 1450), ('pop', 3100)])
    # 뒤에 있는 값을 기준으로 배열하고 싶으면 내부의 원소의 1 번째 인덱스에 있는 값을 가지고 정렬할 것이다 라고 말 할 수 있음!
    # 나 정렬 item 중에 뒤에 있는 원소, 즉 item[1]로 정렬 할거야! 라고 전달 해야함.
    # 그 말을 전달하는 방법이 -> sorted 라는 함수
    # 배열을 받고, key 라는 람다함수(특정 인자를 받아서 어떤 값으로 돌려줄건지 간단한 수식으로 표현)를 받는다.
    # 여기서는 람다함수가 아이템을 받아서 아이템의 첫번째 값, 즉 value 값을 기준으로 배열의 원소들을 정렬하겠다는 의미로 쓰임!
    # sorted(a.items(), key=lambda item: item[1], reverse=True) -> [('classic', 1450), ('pop', 3100)]

    # genre_total_play_dict 정렬, 정렬한 결과는 sorted_genre_play_array 라는 변수에 저장
    # 가장 많은 수록곡이 포함되어 있는 장르들을 순서대로 뽑을 수 있게 됨!
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    # 이거 기반으로 장르별 1순위 2순위 곡들을 결과값에 추가해서 반환
    # genre_index_play_array_dict 에서 pop 장르에서 어떤 곡이 있었는지 보고, 그 친구들에서 플레이 수가 많은 거 대로 배치를 해주면 완성!
    # for 문 이용해서 sorted_genre_play_array 먼저 조회
    # 결과값 담을 배열도 만들기
    result = []

    for genre, _value in sorted_genre_play_array:  # 필요한 건 genre 라서
        # genre 이용해서 밑에 사전에 장르 값을 넣어주면 이게 index_play_array 라는 이름으로 뽑히게!
        index_play_array = genre_index_play_array_dict[genre]  # 장르의 키 값에 있는 값 (value) -> [[1, 600], [4, 2500]]
        # 이 index_play_array 를 다시 한 번 정렬 해서 새로운 변수에 저장 (반복문 안에 들어가는 게 맞음, 각각 정렬해야 하니까)
        # 장르별로 곡의 인덱스와 재생횟수를 저장해 놓은 이 배열을 플레이 순으로 역정렬한 결과를 가진 배열
        # [[4, 2500], [1, 600]]
        # [[3, 800], [0, 500], [2, 140]]
        sorted_index_play_array = sorted(index_play_array, key=lambda item: item[1], reverse=True)

        # 윗 값을 토대로 result 에 추가할 것
        for i in range(len(sorted_index_play_array)):
            # result 에 정렬된 인덱스 플레이 어레이에서 i 번째 원소의 곡의 인덱스를 붙여준다
            # 2곡 씩만 들어갈 수 있게 조건 걸어줌 (장르별로 두 곡!)
            if i > 1:
                break
            result.append(sorted_index_play_array[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
