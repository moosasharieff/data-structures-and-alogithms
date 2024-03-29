

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

        return temp

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
            return None

        # Handling 1+ Node cases
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        # if case only 1 node is left
        if self.length == 0 or self.head is None:
            self.tail = None

        return temp

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


    def set_value(self, index, value):
        """
        :param index:
        :param value:
        :return:
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        """
        Edge cases:
        0. If index provided is out of range
        1. If there is no node in LL
        2. If we are to remove 1st node in LL
        3. If we are remove last node in LL
        4. If we are to remove middle node in the LL
        :param index:
        :return: None or Node<LikedList>
        """
        # 0. If index provided is out of range
        if index < 0 or index > self.length:
            return None

        # 2. If we are to remove 1st node in LL
        if index == 0:
            return self.pop_first()

        # 3. If we are remove last node in LL
        if index == self.length:
            return self.pop()

        # 4. If we are to remove middle node in the LL
        pre = self.get(index-1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """ Reversing this LinkedList """

        # Chaning head and tail of LinkedList
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        # Rotating nodes to reverse
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def find_middle_of_list(self):
        slow = self.head
        fast = self.head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

        return slow

    def is_ll_loop(self):
        """

        :return:Boolean
        """
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            if slow == fast.next:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False

    def convert_binary_to_int(self):
        """
        Converting binary values in the Node to Integer
        :return: int
        """
        n = ''
        temp = self.head
        while temp :
            v = temp.value
            n = n + str(v)
            temp = temp.next
        # converting binary to integer
        return int(n, 2)