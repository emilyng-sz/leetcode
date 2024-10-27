# Slightly better than brute force solution
# Optimal solution requires creating a tree data structure instead of a hashmap

class WordDictionary:

    def __init__(self):
        self.dct = {}

    def addWord(self, word: str) -> None:
        self.dct[word] = 1

    ## I added this function
    def checkWord(self, key, word):
        if len(key) != len(word):
            return False
        else:
            dot_counter = 0
            for i in range(len(word)):
                if word[i] == ".":
                    dot_counter += 1
                if word[i] != "." and word[i] != key[i]:
                    return False
                if dot_counter > 2: return False
        return True

    def search(self, word: str) -> bool:
        n = len(word)
        if word in self.dct:
            return True

        else:
            for key in self.dct.keys():
                if self.checkWord(key, word):
                    return True
            return False 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)