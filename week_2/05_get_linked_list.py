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


def get_linked_list_sum(linked_list_1, linked_list_2):
    sum_1 = _get_linked_list_sum(linked_list_1)
    sum_2 = _get_linked_list_sum(linked_list_2)

    return sum_1 + sum_2


# 문자열로 바꿔서 순서대로 담은 다음 정수형으로 바꿔 계산할 수도 있을 것이고
# 헤드부터 시작해 탐색하는 과정에서 자릿수에 집중해서 계산할 수도 있을 것이다
# sum_1 과 sum_2 중 중복되는 계산이 많으니 함수로 뽀개기 (!!!중복되는 로직 추출!!!)
def _get_linked_list_sum(linked_list):
    # 링크드 리스트에서 저장해 놓은 값은 항상 헤드밖에 없음, 얘네들을 따라가면서 각 값을 더하면서 합계를 내주면 된다.
    # linked_list 의 합계 저장하기 위한 변수, linked_list_sum
    linked_list_sum = 0
    cur = linked_list.head
    while cur is not None:  # 마지막 노드까지 커버해야하니까 cur.next 아닌 cur
        # linked_list_sum 을 10씩 곱해서 더하면 되겠구나 라는 아이디어
        linked_list_sum = (linked_list_sum * 10) + cur.data
        cur = cur.next

    return linked_list_sum


# [6] -> [7] -> [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

# [3] -> [5] -> [4]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
