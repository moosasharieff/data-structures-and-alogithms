

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        """ Creates Stack Object to store in values """
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print(self):
        """ Prints the values in the Stack """
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next



