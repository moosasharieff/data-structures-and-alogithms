

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
        return True

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

    def prepend(self, value):
        """
        Edge cases:
        1. If there is no Node in LL

        :param value:
        :return: True
        """
        new_node = Node(value)
        if self.head is None or self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True


    def pop_first(self):
        """
        Edge cases:
        1. If there is no node in LL
        2. If there is only one node in LL
        3. If there are 1+ nodes in LL
        :return: Boolean
        """
        if self.head is None or self.length == 0:
            return False

        # Handling 1+ Node cases
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # if case only 1 node is left
        if self.length == 0 or self.head is None:
            self.tail = None

        return True

    def get(self, index):
        """

        :param index: <int>
        :return: None or Temp<LinkedList>
        """
        # Condition
        if index < 0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        """
        # Edge Case:
        1. If index is 0 or greater than LL Length
        2. Use prepend to add in beginning
        3. Use append to add in the end
        4. Need logic to add in between
        :param index:
        :param value:
        :return: Boolean
        """
        if index < 0 or index > self.length:
            return False

        # 2. Use prepend to add in beginning
        if index == 0:
            return self.prepend(value)

        # 3. Use append to add in the end
        if index == self.length:
            return self.append(value)

        # 4. Need logic to add in between
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def set_value(self, position, value):
        """
        :param index:
        :param value:
        :return:
        """

        temp = self.get(position - 1)
        temp.value = value
        return temp
