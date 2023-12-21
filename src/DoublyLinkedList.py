import void


class DNode:
    def __init__(self, val=-1):
        """ Creates the Node for Doubly Linked List """
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self, val=-1):
        """ Creates Doubly Linked List """
        new_node = DNode(val)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print(self) -> void:
        """ This method iterates over the Doubly Linked List and prints their value """
        temp = self.head
        while temp :
            print(temp.val)
            temp = temp.next

    def append(self, val):
        """ This method append value to an existing Doubly Linked List
        or creates a new Doubly Linked List if Head is None """
        new_node = DoublyLinkedList(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1


