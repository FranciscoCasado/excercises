import unittest

from cracking.ex_1717.multisearch import multisearch, Node, IndexTrie

class TestMultiSearch(unittest.TestCase):
    def test_multisearch(self):
        
        # B A N A N A,  an, ana
        # 0 1 2 3 4 5
        """
        multisearch("BANANA", ["an", "ana", "ban"]) returns:
        
        { 
            "an": [1, 3],
            "ana": [1, 3],
            "ban": [0]
        }
        """
        
        self.assertTrue(False)


class TestIndexTrie(unittest.TestCase):
    def test_empty_trie(self):
        t = IndexTrie()
        t.insert("asd")
        t.insert("asda")
        t.insert("qwe")
        
        print(t)
        
        self.assertTrue(False)

