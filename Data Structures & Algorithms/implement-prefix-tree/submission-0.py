class TrieNode:
    
    def __init__(self):
        self.childrens = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.childrens[i] == None:
                cur.childrens[i] = TrieNode()
            cur = cur.childrens[i]
        cur.endOfWord = True


    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            i = ord(c) - ord("a")
            if cur.childrens[i] == None:
                return False
            cur = cur.childrens[i]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord("a")
            if cur.childrens[i] == None:
                return False
            cur = cur.childrens[i]
        return True        
        