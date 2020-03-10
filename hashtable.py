class HashTable:
    def __init__(self):
        self.size = 6
        self.table = [None] * 6

    def _get_hash(self, key): #for hashing our keys using a simple ord() function
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def insert(self, key, value):
        hash_key = self._get_hash(key)
        key_value = [key, value]
        
        if self.table[key_hash] = is None:
            self.table[key_hash] = key_value
        else:
            self.table[key_hash].[1] = value


    def retrieve(self, key):
        hash_key = self._get_hash(key)
        if self.table[hash_key]:
            return self.table[hash_key][1] 
