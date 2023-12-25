

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