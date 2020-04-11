import unittest

from HashTable import HashNode, HashTable, anagrams


class TestProject7(unittest.TestCase):

    def test_double_hashing(self):
        ht = HashTable()

        index = ht.double_hashing("abc", True)
        assert (index == 0)

        index = ht.double_hashing("def", True)
        assert (index == 3)

        index = ht.double_hashing("dog", True)
        assert (index == 1)

    def test_insert(self):
        ht = HashTable()

        solution = [HashNode("abc", 4), None, None, HashNode("def", 12), None, None, None]
        ht.insert("abc", 4)
        ht.insert("def", 12)

        assert (ht.size == 2)
        assert (ht.capacity == 7)
        print(ht)

        assert (ht.table == solution)

        ht.insert("abc", 44)  # Reassignment
        assert (ht.table[0].value == 44)

    def test_search(self):
        ht = HashTable()
        ht.insert("frog", 2)
        ht.insert("cow", 12)
        ht.insert("tiger", 1)
        ht.insert("ostrich", 10)

        found_node = ht.search("frog")
        sol_node = HashNode("frog", 2)

        print(ht)
        assert (sol_node == found_node)

    def test_grow(self):
        ht = HashTable()

        for i in range(1, 5):
            ht.insert(i * 'a', i)

        ht.insert('a',3)

        assert ht.size == 4
        assert ht.capacity == 14
        assert ht.prime == 17

    def test_delete(self):
        ht = HashTable(12)
        solution = [None, None, None, None, HashNode(None, None), None,
                    HashNode(None, None), HashNode(None, None), None, None, HashNode("bean", 4), None]

        ht.insert("abc", 1)
        ht.insert("test", 3)
        ht.insert("bean", 4)
        ht.insert("five", 5)

        ht.delete("abc")
        ht.delete("test")
        ht.delete("five")

        print(ht)

        assert (solution == ht.table)
        assert ht.size == 1

    def test_anagrams(self):
        is_anagram = anagrams("listen", "silent")
        assert is_anagram

        is_anagram = anagrams("countryroad", "dountryroad")
        assert not is_anagram

        is_anagram = anagrams("Jumping Jamber", "big men jump jar")
        assert is_anagram

        # Even though all letters are used, the period makes it not an anagram
        is_anagram = anagrams("kinder.", "red ink")
        assert not is_anagram

        is_anagram = anagrams(None, None)
        assert is_anagram

        is_anagram = anagrams(None, "abc")
        assert not is_anagram

        is_anagram = anagrams("", "")
        assert is_anagram

        is_anagram = anagrams("silent", "listen")
        assert is_anagram

        is_anagram = anagrams("silent!.", ".!listen")
        assert is_anagram

        is_anagram = anagrams("Silent!.", ".!listen")
        assert is_anagram

if __name__ == '__main__':
    unittest.main()
