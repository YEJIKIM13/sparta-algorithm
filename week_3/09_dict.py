class Dict:
    def __init__(self):
        self.items = [None] * 8

    # 딕셔너리에 새로운 키와 밸류 추가하기
    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index] = value

    # 키 값에 따른 밸류 값 얻기
    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index]


my_dict = Dict()
my_dict.put("test", 3)
print(my_dict.get("test"))
