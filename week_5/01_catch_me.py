from collections import deque

c = 11
b = 2

# 코니의 위치 변화
# 코니는 처음 위치에서 1초 후 1만큼, 매초마다 이전 이동거리 +1만큼 움직입니다.
# 즉, 증가하는 속도가 1초마다 1씩 증가한다는 소리.
"""
* 코니 속도 *
1 2 3 4 5 6 7 8 9
* 코니 위치 *
(시간에 따라 더해주면 된다)
 1 2 3 4  5  6 
3 4 6 9 13 18 24 ...   -> 간단, 반복문 써서 구하면 되겠지?!
"""
# 브라운의 위치 변화 (핵심), 이건 선택할 수 있는 문제
# B - 1, B + 1, 2 * B
"""
* 브라운 위치 * 
처음 : 2 
1-1. 2 - 1 == 1 (여기서 또 분기 셋 나눠짐) 1-1-1, 1-1-2, 1-1-3
1-2. 2 + 1 == 3 (여기서 또 분기 셋 나눠짐) 1-2-1, 1-2-2, 1-2-3 
1-3. 2 * 2 == 4 (여기서 또 분기 셋 나눠짐) 1-3-1, 1-3-2, 1-3-3 
"""
# 코니와 브라운이 만나려면 브라운의 모든 경우의 수를 비교하면서 몇 초에 언제 도착할 수 있는지를 알아내야 한다!
# 모든 경우의 수를 다 나열해야겠구나 즉, BFS 를 사용하는 문제겠구나.


def catch_me(cony_loc, brown_loc):
    time = 0  # 같은 시간대에 만나야 하기 때문에 시간 개념이 꼭 필요함 (현재 시간 저장해 놓는 변수)
    queue = deque()  # 큐는 미리 임포트했던 deque 를 이용해서 만듦
    # *** 큐에다 초기값인 브라운의 로케이션과 0을 넣는다 ***
    queue.append((brown_loc, 0))  # 위치와 시간을 동시에 담아준다! 위치와 시간이 동시에 일치해야지만 만났다고 할 수 있는 것이기 때문. 그래서 그 둘의 정보를 같이 큐에다 포함시켜줘야 함.
    visited = [{} for _ in range(200001)]  # visited 의 각 원소들은 각 시간 0초에 어느 곳을 갔는지 저장하기 위한 시간

    while cony_loc < 200000:  # 언제까지 반복해야할지 모르겠으니까 처음에는 while 1로 씀, 근데 곧 문제의 조건으로 탈출조건 맞춰줌
        cony_loc += time  # 시간만큼 더해진다고 생각하면 됨 (+1, +2, +3 ... 하니까)

        if time in visited[cony_loc]:
            return time

        # 현재 큐의 길이만큼 반복
        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()  # 저장해줬던 것 꺼내 새로운 변수에 저장

            # 브라운의 위치 (이 셋 중에 뭘 해야할까.) + 추가로 브라운의 위치 또한 조건문에 추가가 되어야 함
            # 이걸 모든 걸 탐색하는 후보군으로 만들어서 전부 탐색시키고 싶다! 그래서 BFS 를 사용하기로 한 것!
            # 그래서 이 모든 경우에 다 수를 구하기 위한 큐를 하나 만들자

            new_time = current_time + 1  # 시간이 갈 테니까 새로운 시간도 정의해줘야
            new_position = current_position - 1  # current_position 을 이용해서 연산해줌 (새로 받아오는 정보 이용해서 연산에 연결지어야!)
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True  # new_position 원소에 new_time 시간에 갔던 곳을 저장
                queue.append((new_position, new_time))  # 각각의 새로운 포지션에 대해서 큐에 아까와 같은 형태로 추가해주기, 갱신!! (세 번 반복의 이유: 모든 경우의 수 구하기 위해 각각의 갈래길 다 만듦)

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

        time += 1  # 그리고 타임은 항상 1초씩 증가하겠지!

    # while 문이 끝났을 때도 없다면 return -1을 해주면 됨
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
