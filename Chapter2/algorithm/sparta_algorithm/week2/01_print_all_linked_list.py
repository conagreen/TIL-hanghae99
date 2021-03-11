# [3] -> [4]
# data, next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)
first_node = Node(4)
node.next = first_node

# print(node.next.data)
# print(node.data)


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):          # 링크드 리스트 append 함수
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        
    def print_all(self):             # 링크드 리스트 모든 원소 출력
        print("hihihi")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

# [3] -> [4] -> [5] -> [6] -> [new]

linked_list = LinkedList(3)

linked_list.append(4)
linked_list.append(5)

linked_list.print_all()