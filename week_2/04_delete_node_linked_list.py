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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        # 노드를 이동하며 보다가 해당 인덱스를 발견하면 리턴하기
        # 마찬가지로 헤드로 시
        node = self.head
        count = 0  # head 부터 시작해서 인덱스 번 만큼 옮겨야 하기 때문에
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head  # 새 노드의 다음 노드가 지금의 head 노드가 될 것
            self.head = new_node  # head 노드는 new_node 라고 지정

        # (인덱스-1) 번째 노드 알아오기, 그래야 그 뒤에 붙임
        prev_node = self.get_node(index - 1)  # 클래스 내부에 있는 다른 함수를 부르기 위해서는 self.함수이름(호출) 하면 된다.
        next_node = prev_node.next  # 임시로 저장해 놓기

        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        # 인덱스 - 1 의 노드 가져와서 그 노드랑 삭제할 노드 다음 노드랑 이어주기
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        prev_node.next = prev_node.next.next




linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.delete_node(1)
linked_list.print_all()

