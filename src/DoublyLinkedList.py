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

    def pop_first(self):
        # No nodes
        if self.head is None or self.length == 0:
            return None
        # When only 1 node
        temp = self.head
        if self.head.next is None or self.length == 1:
            self.head = None
            self.tail = None
        else:
            # When 1+ node
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        """
        # Returns the value of the mentioned index
        :param index:
        :return: None or ListNode
        """
        # Addressing out of range
        if index < 0 or index >= self.length:
            return None

        # Optimising iteration
        temp = self.head
        if index < self.length // 2:
            for _ in range(index):
                temp = temp.next
        else:
            # Traversing from tail to get till index as that is closest.
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp

    def set_value(self, index:int, value:int) -> bool:
        temp = self.get(index)
        if temp :
            temp.val = value
            return True
        return False

    def insert(self, index:int, value:int) -> bool:
        """
        # Conditions to consider:
        1. Out of range
        2. Append
        3. Prepend
        4. Adding node in the middle

        :param index:
        :param value:
        :return: bool
        """
        # 1. Out of range
        if index < 0 or index > self.length:
            return False
        # 2. Appending
        if index == self.length:
            self.append(value)
        # 3. Prepend
        if index == 0:
            self.prepend(value)
        # 4. Adding node in the middle
        else:
            new_node = DNode(value)
            before = self.get(index -1)
            after = before.next

            new_node.prev = before
            new_node.next = after
            before.next = new_node
            after.prev = new_node

            self.length += 1
        return True

    def remove(self, index):
        """
        # Conditions to consider:
        1. Out of range
        2. Remvoe index 0
        3. Remove last index
        4. Remove node in the middle

        :param index:
        :return: Node
        """
        # 1. Out of range
        if index < 0 or index >= self.length:
            return None

        # 2. Remvoe index 0
        if index == 0:
            return self.pop_first()

        # 3. Remove last index
        if index == self.length -1:
            return self.pop()

        # 4. Remove node in the middle
        # Mehthod: 1
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1

        return temp