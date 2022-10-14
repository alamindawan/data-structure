class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinlyLinkList:
    def __init__(self):
        self.head = None

    def add_bigining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = new_node

    def traversing(self):
        node = self.head
        if node is not None:
            while node is not None:
                print(node.data)
                node = node.next

obj = SinlyLinkList()
obj.add_end(10)
obj.add_end(100)
obj.add_end(800)
obj.add_end(900)
obj.traversing()