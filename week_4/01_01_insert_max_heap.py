class MaxHeap:
    def __init__(self):
        self.items = [None]  # 완전 이진 트리 배열로 표현 위해 인덱스 0에는 None 이 들어가는 것 기억하지!

    # 새 노드를 맨 끝에 추가한다.
    # 지금 넣은 새 노드를 부모와 비교한다. 만약 부모보다 크다면 교체한다.
    # 이 과정을 꼭대기까지 반복한다.

    def insert(self, value):
        self.items.append(value)  # 배열로 표현한 힙, 가장 뒤에 새로운 값 추가해주기
        # 이제 여기서 비교하며 위치를 바꿔줘야 하는데, 배열 상태에서는 인덱스를 바꾸는 것
        # 따라서 현재 아이의 인덱스를 알아야! 그래야 앞에 비교하면서 올려주지
        curr_index = len(self.items) - 1

        # 첫 번째 아이가 되면 더 이상 올라갈 데가 없음, 반복은 > 1 까지
        while curr_index > 1:  # curr_index 가 1이 되면 정상을 찍은 거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = curr_index // 2
            if self.items[parent_index] < self.items[curr_index]:
                self.items[parent_index], self.items[curr_index] = self.items[curr_index], self.items[parent_index]
                curr_index = parent_index  # 값 바꿔주고, 현재 인덱스 값 갱신
            else:
                break


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

#     9
#   4   2
# 3
