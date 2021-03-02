class Node:  # 링크드 리스트 구현 시 썼던 클래스
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        # 헤드라는 데이터만 가지고 있고 이 헤드를 통해서 넣고 빼거나 하는 작업을 함
        self.head = None

    # 새로운 노드를 만들고 그 노드가 헤드노드가 된 후, 기존의 헤드노드를 가리키게!
    def push(self, value):
        # 새로운 헤드노드 만들기, 연결짓기 (새로운 헤드의 next 가 현재 헤드)
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop 기능 구현
    # 헤드 값을 없애고 그 것을 리턴(반환), 헤드 교체
    def pop(self):
        # 스택이 비어있다면 리턴
        if self.is_empty():
            return "Stack is empty."
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head  # 여기에 self.head 써주면 바뀐 헤드가 리턴되어서 안 됨. 새로운 변수에 담아서 보존해줘야

    def peek(self):
        if self.is_empty():
            return "Stack is empty."
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        # 불린형으로 리턴해준다면 깔끔!
        # 헤드가 None 인지 아닌지만 검사
        return self.head is None


stack = Stack()  # 스택 인스턴스 생성
stack.push(3)  # 3 push
print(stack.peek())  # 3
stack.push(4)  # 4 push
print(stack.peek())  # 4
stack.push(6)  # 6 push
print(stack.peek())  # 6
print(stack.pop().data)  # 6을 담은 노드 끊어줌, 6을 담은 노드.data 리턴
print(stack.peek())  # 4
print(stack.is_empty())  # False
