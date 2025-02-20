# 링크드 리스트 원소 추가

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
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1

        return node

#          < 원소 추가 구현 >
# 
#     index       next_node
#     ["자갈"]    ["밀가루"] -> ["우편"]
#                 new_node
#             -> ["흑연"] ->
# index.next = new_node
# new_node.next -> next_node

    def add_node(self, index, value):
        new_node = Node(value)  # [6]
        if index == 0:
            new_node.next = self.head # [6] -> [5]
            self.head = new_node # head -> [6] -> [5] -> ....
            return
        else:
            node = self.get_node(index-1) # [5]
            # 어느 코드에서나 index-1처럼 -1이라는 코드가 있으면 0은 어떻게 될까?라는 고민을 해야 함.
            # 따라서! -1에 대한 예외 처리를 해주어야 한다!
            
        next_node = node.next   # [12]
        node.next = new_node    # [5] -> [6]
        new_node.next = next_node   # [6] -> [12]

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(8)

# [5] -> [12] -> [8]
# 추가
# [5] -> [6] -> [12] -> [8]

linked_list.add_node(1, 6)
linked_list.print_all()