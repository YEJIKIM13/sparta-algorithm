class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 노드 전체 개수 구하기
        count = 1  # self.head 의 개수도 반영되어야 하니까
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            count += 1

        # 노드 이동
        cur = self.head
        for i in range(count - k):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

# [6] -> [7] -> [8]
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!