# 링크드 리스트 원소 찾기

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

        return node.data

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(13)
linked_list.append(14)

print(linked_list.get_node(2)) # -> 13을 들고 있는 노드를 반환!