class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    # 1. 맨 뒤에 있는 원소와 루트 노드를 교환한다.
    # 2. 그리고 맨 뒤에 있는 원소 (원래 루트 노드)를 제거한다. (이거 저장해 놓기)
    # 3. 변경된 루트노드와 자식들과 비교한다.
    # 4. 자식이 더 크다면, 그 노드와 교환한다.
    # 5. 이 과정을 자식들이 더 작거나, 바닥 레벨까지 왔으면 멈춘다.
    # 6. 그리고 2번에 저장해둔 노드를 반환하자.

    def delete(self):
        # 1 번째 노드와 len(self.items) - 1 번째 노드를 교환
        self.items[1], self.items[len(self.items) - 1] = self.items[len(self.items) - 1], self.items[1]
        # 맨 뒤에 있는 원소 뽑아버림 (이전에 가장 큰 값이라는 뜻)
        prev_max = self.items.pop()

        # 루트 원소인 인덱스의 1부터 자식 노드들과 비교를 계속해서 시작 (왼쪽 자식부터....)
        # 과정은 마지막 레벨에 도달했을 때! == 자식이 있냐 없냐로 판단, 자신의 인덱스 * 2 가 존재하는 배열의 길이를 넘었으면 자식 노드가 없다라고 판단 가능!
        curr_index = 1  # 인덱스 0 은 None
        while curr_index * 2 < len(self.items) - 1:  # 작을 때까지 반복
            left_child_index = curr_index * 2
            right_child_index = curr_index * 2 + 1
            if self.items[curr_index] < self.items[left_child_index]:  # 이라면 값 교체
                self.items[curr_index], self.items[left_child_index] = self.items[left_child_index], self.items[curr_index]
                curr_index = left_child_index  # 현재 인덱스 갱신
            elif self.items[curr_index] < self.items[right_child_index]:  # 이라면 값 교체
                self.items[curr_index], self.items[right_child_index] = self.items[right_child_index], self.items[curr_index]
                curr_index = right_child_index  # 현재 인덱스 갱신
            else:  # 위의 두 경우가 아닐 경우 반복을 멈춤
                break

        return prev_max  # 8 을 반환해야 합니다.


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
