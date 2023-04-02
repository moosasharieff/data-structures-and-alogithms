
"""
# Stack Functionalities

1. Push - Insert element
2. Pop - Delete element
3. Top - Access top (only) element

------
4. Size - length of stack
5. isEmpty - boolean result
"""

class Stack:

    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Hey, Stack is already Empty!")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey, Stack is Empty")
            return
        return self.__data[-1]

    def size(self):
        return len(self.__data)

    def isEmpty(self):
        return self.size() == 0

    def __str__(self):
        pass

    def __repr__(self):
        pass