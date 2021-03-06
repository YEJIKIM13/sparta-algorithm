class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        # 비었는지 안 비었는지 여부에 따라 예외처리를 따로 해주어야 한다.
        # .next 가 문제를 일으킬 것임...-> use if
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        # 맨 앞의 원소 먼저 빠
        if self.is_empty():
            return "Queue is empty."

        deleted_node = self.head
        self.head = self.head.next  # 주의!

        return deleted_node.data

    def peek(self):
        if self.is_empty():
            return "Queue is empty."

        return self.head.data

    def is_empty(self):
        return self.head is None


# 새 인스턴스 생성
queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())  # 3을 빼면서 리턴
print(queue.peek())
print(queue.is_empty())
