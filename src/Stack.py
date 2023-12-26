

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

    def push(self, value):
        """ Adds or appends value to the Stack """
        new_node = Node(value)
        # if Stack is empty
        if not self.top:
            self.top = new_node
        else:
            # Appending value to existing Stack
            new_node.next = self.top
            self.top = new_node
        self.height += 1


    def pop(self):
        """ Removes the 1st node from the Stack """
        # if Stack is empty
        if not self.top:
            return None
        # if Stack contains Nodes
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp # as poped value is still present in temp