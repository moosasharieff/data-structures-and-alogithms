

class Node:
    """ create a Node """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """ LinkedList Methods """
    def __init__(self, value):
        # Create a LinkedList with 1 node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print(self):
        # prints the linkedlist
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # Edge case : 1. if no node exists, create a new node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def pop(self):
        """
        # Removes the last node from the existing LL (>2 nodes)

        # Edge case:
        1. If there is no node in the LL
        2. If there is only 1 node in the LL
        """
        # Edge case : 1. If there is no node in the LL
        if self.length == 0 or self.head is None:
            return None

        # Removes the last node from the existing LL (>2 nodes)
        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        # Below condition runs when temp has reached the last Node
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        # Edge case 2. If there is only 1 node in the LL
        if self.length == 0:
            self.head = None
            self.tail = None


