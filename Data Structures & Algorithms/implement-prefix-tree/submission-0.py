class TreeNode:
    def __init__(self):
        self.prefix = {}
        self.finish = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        if self.search(word):
            return
        node = self.root
        for char in word:
            if char not in node.prefix:
                node.prefix[char] = TreeNode()
            node = node.prefix[char]
        node.finish = True      


    def search(self, word: str) -> bool:
        node = self.root
        for i in range(len(word)):
            char = word[i]
            if char not in node.prefix:
                return False
            node = node.prefix[char]
        
        return node.finish
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.prefix:
                return False
            node = node.prefix[char]
        return True
        
        