class TrieNode:
    def __init__(self):
        self.children = [None] * 26 # TrieNode has empty array of 26 (because only small letters in problem)
        self.isEnd = False # And one 


class Trie:
    def __init__(self):
        self.root = TrieNode() # A TrieNode would be put inside when trie is called

    def insert(self, word):
        curr = self.root # curr pointer is set at root
        for i in range(len(word)):  
            c = word[i]         # Storing current char at c
            index = ord(c) - ord('a') # It'll get the index value
            if not curr.children[index]: # if the char's index is empty in children
                curr.children[index] = TrieNode() # create an empty TreeNode at that place
            curr = curr.children[index] # Move current pointer to the children
        curr.isEnd = True # After inserting the word, set boolean flag to True (Word exist)

    def search(self, word):
        curr = self.root
        for i in range(len(word)):
            c = word[i]
            index = ord(c) - ord('a')
            if not curr.children[index]: # If at child's desirable index, nothing is there; return False
                return False
            curr = curr.children[index] # Passing the curr pointer to next child
        return curr.isEnd #If the word is there, curr.isEnd would be true else false

    def startsWith(self, prefix): # Same thing as search
        curr = self.root
        for i in range(len(prefix)):
            c = prefix[i]
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert(word)
# search_result = trie.search(word)
# startsWith_result = trie.startsWith(prefix)
