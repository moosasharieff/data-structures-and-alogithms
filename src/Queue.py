

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
            self.last.next = new_node
            self.last = new_node
        self.length += 1