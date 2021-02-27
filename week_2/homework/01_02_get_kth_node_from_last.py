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

    # 포인터 두 개 이용해서 해결하기
    # 1. 노드를 두 개 잡는다
    # 2. 한 노드를 다른 노드보다 k 만큼 떨어지게 한다.
    # 3. 그리고 계속 한 칸씩 같이 이동한다.
    # 4. 만약 더 빠른 노드가 끝에 도달했다면
    # 5. 느린 노드는 끝에서 k 만큼 떨어진 노드가 되므로 바로 반환하자.

    def get_kth_node_from_last(self, k):
        slow = self.head
        fast = self.head

        for i in range(k):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

# [6] -> [7] -> [8]
print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!