# data, next (뭐가 필요하지?)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)  # Node 클래스 이용해 node 생성
first_node = Node(4)
node.next = first_node  # 연결


# 링크드 리스트, 가지고 오는 데이터는 헤드 노드만 가지고 와도 된다
class LinkedList:
    # data 를 받고, self.head 에 해당 데이터를 들고 있는 노드를 생성해서 넣어주면 됨! (헤드 노드만 가지고 오면 되니까!!)
    def __init__(self, data):
        self.head = Node(data)  # 노드 생성하고 그 노드에 data 값 넣어준 것을 헤드 노드에 넣으면 됨, 방금 생성한 노드가 헤드노드로써 저장이 되겠지 바로!

    def append(self, data):
        # self.head.next = Node(data) -> 이러면 안됨! 하고 싶은 건 제일 뒤에 붙이는 것
        # head 노드를 계속 이동시키다가 헤드 노드.next 에 새로운 노드 지정함.
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)  # 제일 뒤에 오면 그 때 노드 붙임!
        print(cur.data)

    def print_all(self):
        print("모든 노드를 출력합니다.")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next



linked_list = LinkedList(3)
print(linked_list, linked_list.head, linked_list.head.data, linked_list.head.next)  # 차이점 알기!
linked_list.append(4)  # 데이터를 넣어주도록 만들었음
linked_list.append(5)  # 맨 마지막에 있는 노드의 데이터를 출력한 것이어서. cur.next = Node(data) 는 그 다음에 새로운 데이터를 받은 거다.
linked_list.print_all()