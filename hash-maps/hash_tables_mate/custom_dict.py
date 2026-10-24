from typing import Any, Hashable, Generator


class Dictionary:
    def __init__(self):
        self._capacity = 8  # inital capacity
        self._hash_table = [None] * 8  # [(key, hash(key), value), (...),..] - a list of tuples
        self._load_factor = 2 / 3  # factor for triggering resizing mechanism (0.75)
        self._size = 0  # keep track of the _size

    # 1.
    def _get_node_index(self, key: Hashable, capacity: int) -> int:

        """
        Finds the index of a key in the underlying list data structure.

        Given a key, this method will calculate the initial index of that key 
        in the underlying list and then linear probe until it finds 
        an empty slot or a slot with the same key. 
        The index of that slot is then returned.

        Time complexity: O(n) where n is the capacity of the dictionary.
        """
        node_index = hash(key) % capacity  # find the inital index

        # recompute index if needed
        # while the slot is occupied and, the key stored in this slot 
        # is different than the given 'key', it keeps looking for an empty slot
        while (
            self._hash_table[node_index]  # 1. check the slot is empty
            # [(key, hash(key), value)], extract existing key to check it
            and self._hash_table[node_index][0] != key  # 2. check the given key is equal to existing
        ):
            # linear probing, since collision occured (object not equal but their hashes are the same)
            node_index = (node_index + 1) % capacity

        return node_index  # returns either, the index of the empty slot or for the same key

    # 2.
    def _resize(self) -> None:
        """
        Doubles the _size of the hash table when load factor reaches 2/3.

        This method is called when adding a new key-value pair and the load factor
        (the ratio of filled slots to total slots) is greater than or equal to 2/3.
        The method creates a new hash table with double the capacity of the old one,
        then re-calculates the new indices of the existing items using the new capacity.
        Finally, it updates the hash table and capacity of the dictionary with the new ones.
        """
        new_capacity = self._capacity * 2  # double the hash table _size
        new_hash_table = [None] * new_capacity  # create new hash table

        for node in self._hash_table:  # re-calculate new indices for existing items
            if node:
                key, *_ = node  # extract key
                new_node_index = self._get_node_index(key, new_capacity)  # get new index, checking with probing where necessary
                new_hash_table[new_node_index] = (key, *_)  # store existing item under new index in new hash table

        # use new hash table & capacity now
        self._hash_table = new_hash_table
        self._capacity = new_capacity

    # 3.
    def __setitem__(self, key: Hashable, value: Any) -> None:
        """
        Adds a new key-value pair to the dictionary or updates the existing one.

        This method takes a key and a value as arguments and adds them to the dictionary.
        If the key already exists in the dictionary, it updates the existing value.
        Also, it checks if the load-factor is exceeded and re_sizes the dictionary if needed.
        """
        node_index = self._get_node_index(key, self._capacity)
        # create a node content
        node = (key, hash(key), value)

        if self._hash_table[node_index] and self._hash_table[node_index][0] == key:
            self._hash_table[node_index] = node  # update if the key equals to existing one
        else:
            # if empty slot, just store the new node
            self._hash_table[node_index] = node
            self._size += 1  # keep track of _size
        
        # check if the load-factor is not exceeded
        if self._size / self._capacity >= self._load_factor:
            self._resize()

    # 4.
    def __getitem__(self, key: Hashable) -> Any:
        """
        Retrieves a value from the dictionary by a given key.

        This method takes a key as an argument and returns the corresponding value.
        If the key does not exist in the dictionary, it raises a KeyError.
        """
        node_index = self._get_node_index(key, self._capacity)

        if self._hash_table[node_index]:
            return self._hash_table[node_index][2]

        raise KeyError(f"Key {key} does not exist")

    # 5.
    def __delitem__(self, key: Hashable) -> None:
        """
        Deletes a key-value pair from the dictionary by a given key.

        This method takes a key as an argument and deletes the corresponding key-value pair.
        If the key does not exist in the dictionary, it raises a KeyError.
        """
        node_index = self._get_node_index(key, self._capacity)

        try:
            if self._hash_table[node_index]:
                self._hash_table[node_index] = None
                self._size -= 1
        except KeyError:
            return f"Key {key} does not exist"
        
    def __iter__(self) -> Generator[Any, None, None]:
        """
        Returns an iterator over the keys in the dictionary.
        """
        
        for node in self._hash_table:
            if node:
                yield node[0]
    
    def __len__(self) -> int:
        return self._size


d = Dictionary()
d["item1"] = "Hello"
print(len(d))
print(d["item1"])
