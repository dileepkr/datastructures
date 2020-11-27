class Map:
    def __init__(self) -> None:
        self.length = 11
        self.slots = [None] * self.length
        self.data = [None] * self.length

    def put(self, key, val):
        hash_val = self.hash_function(key, self.length)
        if not self.slots[hash_val]:
            self.slots[hash_val] = key
            self.data[hash_val] = val
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = val
            else:
                rehash_val = self.rehash_function(hash_val, self.length)
                while self.slots[rehash_val] != None and self.slots[rehash_val] != key:
                    if rehash_val == hash_val:
                        raise Exception(f"cannot insert key into the hash map")
                    rehash_val = self.rehash_function(rehash_val, self.length)
                if not self.slots[rehash_val]:
                    self.slots[rehash_val] = key
                    self.data[rehash_val] = val
                elif self.slots[rehash_val] == key:
                    self.data[rehash_val] = val

    @staticmethod
    def hash_function(key, size):
        return key % size
    
    @staticmethod
    def rehash_function(old_hash_key, size):
        return (old_hash_key+1) % size
    
    def get(self, key):
        hash_val = self.hash_function(key, self.length)
        if self.slots[hash_val] == key:
            return self.data[hash_val]
        else:
            rehash_val = self.rehash_function(hash_val, self.length)
            while rehash_val != hash_val:
                if self.slots[rehash_val] == key:
                    return self.data[rehash_val]
                rehash_val = self.rehash_function(rehash_val, self.length)
            raise Exception(f"Key not found in the current hashmap")

    def delete(self, key):
        hash_val = self.hash_function(key=key, size=self.length)
        if key == self.slots[hash_val]:
            self.slots[hash_val] = None
            self.data[hash_val] = None
            return True
        else:
            rehash_val = self.rehash_function(hash_val, self.length)
            while rehash_val != hash_val:
                if self.slots[rehash_val] == key:
                    self.slots[rehash_val] = None
                    self.data[rehash_val] = None
                    return True
                rehash_val = self.rehash_function(rehash_val, self.length)
            if rehash_val == hash_val:
                raise Exception(f"Key {key} not found in the dictionary, Delete operation aborted.")

    def len(self):
        length = 0
        for key in self.slots:
            if key:
                length+=1
        return length

    def __contains__(self, key):
        try:
            if self.get(key):
                return True
        except:
            return False

    def keys(self):
        return [key for key in self.slots if key]

    def values(self):
        return [self.data[key] for key in self.slots if key]

    def __getitem__(self, key):
        return self.get(key=key)

    def __setitem__(self, key, data):
        self.put(key=key, val=data)

    def __repr__(self) -> str:
        return str(dict(zip(self.slots, self.data)))

if __name__ == "__main__":
    h1 = Map()
    h1[54]="cat"
    h1[26]="dog"
    h1[93]="lion"
    h1[17]="tiger"
    h1[77]="bird"
    h1[31]="cow"
    h1[44]="goat"
    h1[55]="pig"
    h1[20]="chicken"
    print("__"*30)
    print(f"slots: {h1.slots}")
    print(f"data: {h1.data}")
    # print({k:v for k, v in zip(h1.slots, h1.data)})
    h1[20] = "duck"
    print("__"*30)
    print(f"slots: {h1.slots}")
    print(f"data: {h1.data}")
    h1.delete(20)
    print("__"*30)
    print(f"slots: {h1.slots}")
    print(f"data: {h1.data}")

    print(77 in h1)
