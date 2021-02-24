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


# 문자열로 바꿔서 순서대로 담은 다음 정수형으로 바꿔 계산할 수도 있을 것이고
# 헤드부터 시작해 탐색하는 과정에서 자릿수에 집중해서 계산할 수도 있을 것이다
def get_linked_list_sum(linked_list_1, linked_list_2):
    # 링크드 리스트에서 저장해 놓은 값은 항상 헤드밖에 없음, 얘네들을 따라가면서 각 값을 더하면서 합계를 내주면 된다.
    # linked_list_1의 합계 저장하기 위한 변수, sum_1
    sum_1 = 0
    cur_1 = linked_list_1.head
    while cur_1 is not None:  # 마지막 노드까지 커버해야하니까 cur_1.next 아닌 cur_1
        # sum_1을 10씩 곱해서 더하면 되겠구나 라는 아이디어
        sum_1 = (sum_1 * 10) + cur_1.data
        cur_1 = cur_1.next

    sum_2 = 0
    cur_2 = linked_list_2.head
    while cur_2 is not None:  # 마지막 노드까지 커버해야하니까 cur_2.next 아닌 cur_2
        # sum_2을 10씩 곱해서 더하면 되겠구나 라는 아이디어
        sum_2 = (sum_2 * 10) + cur_2.data
        cur_2 = cur_2.next
    return sum_1 + sum_2


# [6] -> [7] -> [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

# [3] -> [5] -> [4]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)


print(get_linked_list_sum(linked_list_1, linked_list_2))