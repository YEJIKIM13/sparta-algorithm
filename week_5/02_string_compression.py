input = "abcabcabcabcdededededede"

# 1로 잘라야 할지, 2로 잘라야 할지, 3으로 잘라야 할지... 어떻게 패턴을 분석하면 좋을지에 대해 생각할텐데, 모든 경우를 다 봐야하므로 경우의 수 파악이어야 함!
# 문자열을 자르는 방법은 길이 별로 나뉠 수 있음!


def string_compression(string):
    n = len(string)  # 문자열의 길이를 변수에 저장
    compression_length_array = []

    # 문자열 슬라이싱 전에 몇의 사이즈로 쪼갤 건지 저장하기 위해 split_size 라는 변수에 1부터 반복 (0부터는 필요 없으니)
    for split_size in range(1, n//2 + 1):
        """
        # 문자열 쪼개기
        splited = []
        for i in range(0, n, split_size):  # 인덱스 이용해서 쪼개고
            splited.append(string[i:i + split_size])  # 그리고 <- 이 친구를 splited 에다가 추가해주면 됨
        """
        splited = [
            # 안에다가 string 을 어떻게 넣을 건지 정의하기.
            # 어떻게 i 를 설정? -> for 문을 뒤에다 써 줌
            string[i:i + split_size] for i in range(0, n, split_size)  # 위의 식과 동일하게 사용 가능
        ]
        # 이제 이 쪼개진 걸 압축할 수 있는지 아닌지 여부 알아내야 함
        # splited 에서 0번째랑 1번째랑 비교해 -> splited[0] splited[1]
        # 다시 splited[1] 과 splited[2] 비교해, 이렇게 하면서 몇 번이 반복되었는지 기억해야 함 -> 변수 count

        compressed = "" # 압축해서 표현한 문자를 다시 한 번 변수에다가 저장을 해서 공통으로 써줘야 함
        count = 1  # 이전 값과 자기 값을 비교하는 것이기 때문에 이미 나는 나와 있음! 그래서 1로 초기화

        for j in range(1, len(splited)):  # 1부터 시작하는 이유: 이전 값이랑 지금 값이랑 비교하기 위해 prev, cur 변수 둠
            prev, cur = splited[j - 1], splited[j]
            if prev == cur:
                count += 1
            else:  # 이전 문자와 다를 때 (근데 여기서 카운트가 1개일 수도 있고 1개 이상일 수도 있음)
                if count > 1:
                    compressed += (str(count) + prev)
                else:
                    compressed += prev
                count = 1  # 반복이 끝나버리는 순간에는 count 를 다시 1로 초기화 시켜야 함

        # 맨 마지막에 남은 것도 앞이랑 똑같은지 비교해줘야 함 -> 마지막 끝난 카운트가 몇이었느냐를 또 봐주면 됨
        if count > 1:  # (반복되었다는 뜻)
            compressed += (str(count) + splited[-1])  # 여기서 문자열은 제일 마지막에 있는 꼬다리 값
        else:
            compressed += splited[-1]
        # print(compressed) 해서 중간 결과 살펴봐도 좋음!

        # 원하는 건 이 문자열 중에 가장 길이가 짧은 것 (가장 최소인 것) -> 가장 최소인 길이들을 모아놓는 변수가 있어야. ** 변수 사용을 잘해야!! **
        compression_length_array.append(len(compressed))

    return min(compression_length_array)  # 최솟값 리턴


print(string_compression(input))  # 14 가 출력되어야 합니다!
