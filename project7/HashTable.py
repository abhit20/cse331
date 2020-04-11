"""
Project 7 - Hash Tables
CSE331 - F19
Created By: Wendy Fogland
"""

class HashNode:
    """
    DO NOT EDIT
    """

    def __init__(self, key, value, available=False):
        self.key = key
        self.value = value
        self.is_available = available

    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

    def __eq__(self, other):
        return self.key == other.key and self.value == other.value


class HashTable:
    """
    Hash Table Class
    """

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity=7):
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: how much the hash table can hold
        """

        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        for prime in self.primes:
            if self.capacity <= prime:
                self.prime = prime
                break

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """

        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """

        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    def _is_available(self, j):
        """
        DO NOT EDIT
        Check if the index in the table is available/empty
        :param j: index in the table
        :return: True if available or empty, false otherwise
        """
        return self.table[j] is None or self.table[j].is_available is True

    def hash_first(self, key):
        """
        DO NOT EDIT
        Converts key, a string, into a bin number for the hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if val is an empty string
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def hash_second(self, key):
        """
        Hashes key based on prime number for double hashing
        DO NOT EDIT
        :param key: key to be hashed
        :return: a hashed value
        """

        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        hashed_value = self.prime - (hashed_value % self.prime)
        if hashed_value % 2 == 0:
            hashed_value += 1

        return hashed_value

    def double_hashing(self, key, inserting=False):
        """
        Given a key, return the index in which the key can be inserted into the hash table
        :param key: The key to find
        :param inserting: True if inserting, False if deleting
        :return: Index of the node if key exists, else index of next empty bucket
        """
        h1 = self.hash_first(key)
        if self.table[h1] is not None:
            if self.table[h1].key == key:
                return h1
            h2 = self.hash_second(key)
            i = 0
            index = (h1 + (i * h2)) % (self.capacity)
            while self.table[index] is not None and index < self.capacity:
                if self.table[index].key == key:
                    return index
                i += 1
                index = (h1 + (i * h2)) % (self.capacity)
            return index
        return h1

    def insert(self, key, value):
        """
        Inserts a HashNode into the hash table using key and value
        :param key: The key to insert
        :param value: The value to insert
        :return:
        """
        index = self.double_hashing(key,inserting=True)
        if self._is_available(index) is True:
            self.size += 1
        self.table[index] = HashNode(key,value)
        self.grow()

    def search(self, key):
        """
        Search for the HashNode with the given key in the hash table.
        :param key: The key to find
        :return: the node with the given key if found, None if not found
        """
        index = self.double_hashing(key)
        return self.table[index]

    def grow(self):
        """
        Increase the capacity of the existing hash table
        :return:
        """
        if (self.size/self.capacity) >= 0.4:
            self.size = 0
            self.capacity *= 2
            for prime in self.primes:
                if self.capacity < prime:
                    self.prime = prime
                    break
            self.rehash()

    def rehash(self):
        """
        Rehashes all nodes in table except the deleted nodes
        :return:
        """
        old = self.table
        self.table = [None] * int(self.capacity)
        for node in old:
            if node is not None:
                if node.is_available is False:
                    self.insert(node.key, node.value)

    def delete(self, key):
        """
        Deletes the HashNode from the HashTable
        :param key: The key to delete
        :return:
        """
        node = self.search(key)
        if node is not None:
            node.key = None
            node.value = None
            node.is_available = True
            self.size -= 1

def anagrams(string1, string2):
    """
    Compares to see if the two strings are anagrams
    :param string1: The first string
    :param string2: The second string
    :return: True if the strings are anagrams, else False
    """
    ht = HashTable(1)

    if string1 is None and string2 is None:
        return True

    string = string1
    count = 1
    while count < 3:
        if string is not None:
            for ch in string.lower():
                if ch != " ":
                    search_node = ht.search(ch)
                    if search_node is not None:
                        ht.insert(ch, search_node.value+1)
                    else:
                        ht.insert(ch, 1)
        string = string2
        count += 1

    for node in ht.table:
        if node:
            if node.value % 2 != 0:
                return False
    return True