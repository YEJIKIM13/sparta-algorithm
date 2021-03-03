genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


# 뭐가 필요한지 생각해보자!!
def get_melon_best_album(genre_array, play_array):
    genre_all_play_dict = {}
    genre_index_play_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        # 있다면 += 없다면 =
        if genre not in genre_all_play_dict:
            genre_all_play_dict[genre] = play
            genre_index_play_dict[genre] = [[i, play]]  # 2차원 배열 보여줘야 하니까 [[]]로 써줘야 함!
        else:
            genre_all_play_dict[genre] += play
            genre_index_play_dict[genre].append([i, play])

    # 정렬 과정
    genre_all_play_array_sort = sorted(genre_all_play_dict.items(), key=lambda item: item[1], reverse=True)

    result_array = []
    # (result_array 에 원하는 값 추가하는 과정)
    # genre_all_play_array_sort 돌면서 키 값 받아오기 (장르 받아와야 하니까...)
    # 장르 이용해 인덱스와 플레이 받아오기
    # 받아온 것 정렬
    # 내부에서 배열로 받아온 정렬된 genre_index_play_dict 의 [i][0] 받아오면 된다!
    for genre, _value in genre_all_play_array_sort:
        index_play_array = genre_index_play_dict[genre]  # 예: [1, 600], [4, 2500]
        index_play_array_sort = sorted(index_play_array, key=lambda item: item[1], reverse=True)  # [4, 2500], [1, 600]
        for i in range(len(index_play_array_sort)):
            if i >= 2:  # 인덱스 0, 인덱스 1 까지 (두 개) 받아야 하니까
                break
            result_array.append(index_play_array_sort[i][0])  # 인덱스만 받아옴

    return result_array


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
