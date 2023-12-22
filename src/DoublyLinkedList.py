import void

from src.stacks.StackUsingLinkedList import ListNode


class DNode:
    def __init__(self, val=-1):
        """ Creates the Node for Doubly Linked List """
        self.val = val
        self.next = None
        self.prev = None

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
        new_node = DNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def pop(self):
        # handling no nodes
        if self.head is None or self.length == 0:
            return None
        temp = self.tail
        # handling single Node
        if self.head.next is None or self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1

        return temp


    def prepend(self, val):
        new_node = DNode(val)
        # When no node
        if self.head is None or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # When 1 or more nodes
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
