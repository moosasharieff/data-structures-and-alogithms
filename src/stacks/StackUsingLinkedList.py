

class ListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class StackLL:

    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self, data):

        newNode = ListNode(data)
        newNode.next = self.__head

        self.__head = newNode
        self.__count += 1

        return data

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
            return

        val = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1

        return val

    def top(self):
        return self.__head.data

    def size(self):
        return self.size()

    def isEmpty(self):
        return self.size() == 0




