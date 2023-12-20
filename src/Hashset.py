#
# class MyHashSet(object):
#
#     def __init__(self):
#         # Define the size of the Hashtable
#         self.size = 10000
#         self.table = [None] * self.size
#
#     def cal_hash_value(self, key):
#         return key % self.size
#
#     def add(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         hv = self.cal_hash_value(key)
#         if self.table[hv] == None:
#             self.table[hv] = key
#         else:
#             # check if it contains
#             for i, val in enumerate(self.table[hv]):
#                 if key != val:
#                     self.table[hv].append(key)
#             # if there is no key in the list of that hash table,
#             # append the key to that hash table
#
#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
#         # Checks and removes the key only if there is any value in hash location
#         hv = self.cal_hash_val(key)
#         if self.hash[hv] != None:
#             self.table[hv].remove(key)
#
#     def contains(self, key):
#         """
#         :type key: int
#         :rtype: bool
#         """
#         hv = self.cal_hash_value(key)
#
#         if self.table[hv] == None:
#             return False
#         else:
#             if key == self.table[hv]:
#                 return True
#         return False
#
#     # Your MyHashSet object will be instantiated and called as such:
#     # obj = MyHashSet()
#     # obj.add(key)
#     # obj.remove(key)
#     # param_3 = obj.contains(key)


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] == None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] != None:
            while key in self.table[hv]:
                self.table[hv].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        """
        hv = self.calculate_hash_value(key)

        if self.table[hv] != None:
            return key in self.table[hv]
        return False


class PracisedHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size

    def calculate_hash_value(self, key):
        return key % self.size

    def add(self, key):
        hv = self.calculate_hash_value(key)
        if self.table[hv] is None:
            self.table[hv] = [key]
        else:
            self.table[hv].append(key)

    def remove(self, key):
        hv = self.calculate_hash_value(key)
        if self.table[key] is not None:
            while key in self.table[hv]:
                self.table[hv].remove(key)


    def contains(self, key):
        hv = self.calculate_hash_value(key)

        if self.table[hv] is not None:
            if key in self.table[hv]:
                return True
        return False



# Your MyHashSet object will be instantiated and called as such:
obj = PracisedHashSet()
obj.add(1)
obj.add(1)
obj.remove(1)
param_3 = obj.contains(1)
print(param_3)
obj.add(2)
param_3 = obj.contains(2)
print(param_3)

