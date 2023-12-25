

class Node:
    def __init__(self, value):
        """ Creates a node for the Queue """
        self.next = None
        self.value = value

class Queue:
    def __init__(self, value):
        """ Creates a Queue Object to store data """
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print(self):
        """ Prints the values in the Queue Object """
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        """ Adds value to the queue """
        new_node = Node(value)
        # if the queue is empty
        if not self.first:
            self.first = new_node
            self.last = new_node
        else:
            # Adding value to queue having values
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """ Remove the value from the queue
        Things to consider :
        1. Removing when Queue is empty
        2. Removing when Queue has only 1 node
        3. Removing when Queue has 1+ nodes
        """
        # 1. Removing when Queue is empty
        if not self.first or self.length == 0:
            return None

        temp = self.first
        # 2. Removing when Queue has only 1 node
        if not self.first.next or self.length == 1:
            self.first = None
            self.last = None
        else:
            # 3. Removing when Queue has 1+ nodes
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp