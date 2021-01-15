https://www.algoexpert.io/questions/Suffix%20Trie%20Construction

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)
	
	def insert_substring(self,i, string):
		node = self.root
		for letter in string[i:]:
			if letter not in node:
				node[letter] = {}
			node = node[letter]
		node[self.endSymbol] = True
		
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
			self.insert_substring(i,string)
		print(self.root)

    def contains(self, string):
        node = self.root
		for letter in string:
			if letter not in node:
				return False
			else:
				pass
			node = node[letter]
		return self.endSymbol in node
