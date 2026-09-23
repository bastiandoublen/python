class SimpleHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        h = self._hash(key)
        self.table[h].append((key, value))

    def get(self, key):
        h = self._hash(key)
        for k, v in self.table[h]:
            if k == key:
                return v
        return None

ht = SimpleHashTable()
ht.insert("apple", 100)
ht.insert("banana", 200)

print("Get apple:", ht.get("apple"))
print("Get banana:", ht.get("banana"))
