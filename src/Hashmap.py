class Listnode:

    def __init__(self, key=-1, value=-1):
        self.key = key
        self.value = value
        self.next = None


class Hashmap:
    def __init_(self):
        # create the empty hashmap table
        self.map = [[Listnode] for _ in range(1000000)]

    def hash_value(self, key):
        """"
        Finds the hash value for the provided key
        :type int
        :rtype int 
        """
        return key % len(self.map)

    def put(self, key:int, value:int) -> None:
        """

        :param key:
        :param value:
        :return: None
        :description: Updates the value on the key if its same or add the value to the node
        """
        hv = self.hash_value(key)
        curr = self.map[hv]

        while curr.next:
            if curr.next.key == key:
                # Update the curr.next.value with new value
                curr.next.value = value
            curr = curr.next
        # create a new node and add to the curr.next
        curr.next = Listnode(key, value)


    def get(self, key:int, value:int) -> int:
        """

        :param key:
        :param value:
        :return: int
        :description: Returns value of the key if present else returns -1
        """
        hv = self.hash_value(key)
        curr = self.map[hv]

        while curr.next:
            if curr.next.key == key:
                # returns the value if key is found
                return curr.next.value
            curr = curr.next
        # return -1 if key is not found
        return -1

    def remove(self, key:int, value:int) -> bool:
        hv = self.hash_value(key)
        curr = self.map[hv]

        # Proceeding only if null node and node next to it has key:value or not
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False