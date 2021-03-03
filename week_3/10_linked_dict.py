class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):  # 이 값들을 모두 저장하는 형식으로 갈 거라서 키와 밸류 다 있어야하고, 각각의 튜플을 추가하는 방식이라고 생각하자
        # self.items 맨 뒤에 새로운 튜플 붙임
        self.items.append((key, value))

    # 튜플 내에서 값을 찾기 위해선 키가 또 하나 필요함
    def get(self, key):  # 왜냐면 키에 따라서 값이 달라지기 때문
        # items 하나하나 돌면서 키와 동일하다면 그 값을 반환
        for k, v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self):
        # constructor 에서 미리 기존의 데이터를 담아 놓을 공간을 만들어 놔야 하는데
        # 이번에는 단순한 배열이 아니라 링크드 리스트를 쓸 것이기 때문에
        # 8번 반복해서 self.items 에 LinkedTuple (위에서 만들었던 자료구조) 그 녀석을 넣어보도록 하자
        self.items = []  # [LinkedTuple(), LinkedTuple(), ... , LinkedTuple()] -> 각 원소의 키가 동일하면 똑같은 LinkedTuple 안에서 값들이 쭉쭉쭉 늘어난다는 구조...
        for i in range(8):
            self.items.append(LinkedTuple())

    # 키랑 밸류를 넣으면 키에 대한 items 를 찾아서 밸류 값을 추가해주는 함수
    def put(self, key, value):
        # 키를 가지고 인덱스 찾기
        index = hash(key) % len(self.items)
        # 해당하는 인덱스에 밸류 넣기 -> self.items[index] = value 해주고 싶은
        # 근데 지금은 self.items[index]에 LinkedTuple 이 들어 있음
        # LinkedTuple, [] <- 여기에
        # [(key, value)] 이렇게 넣어주고 싶은데, 이렇게 넣어주는 메소드를 이미 LinkedTuple 에서 만들어 놨음 .add 메소드
        # 해당하는 인덱스에 밸류 넣기
        self.items[index].add(key, value)

    # 키를 주면 해당하는 값을 반환해주는 메소드
    def get(self, key):
        index = hash(key) % len(self.items)
        # items[index] 에 있는게 LinkedTuple (해당하는 자료구조가 뭔지 잘 살펴보자!!!)
        # 하나 더 나아가서 LinkedTuple get 메소드를 통해 키까지 넣어줘야 value 알 수 있음
        return self.items[index].get(key)
