class MyArray:
    def __init__(self):
        self.length = 0  # used for specifying index as the key & keep track of length
        self.data = {}  # store data

    def get_item(self, index):  # O(1)
        # return item under index
        if 0 > index >= self.length:
            raise IndexError("Index out of range")
        return self.data[index]

    def append_item(self, item):  # O(1)
        # store item at the end, increment self.length
        self.data[self.length] = item
        self.length += 1  # keep track of the length & used as the index for the next item to append
        return self

    def pop_item(self):  # O(1)
        # ref last item, remove from data, decrement self.length, return last item
        if self.length == 0:
            raise IndexError("Pop from empty array")

        last_item = self.data[self.length - 1]  # 'self.length - 1' is the last item index

        del self.data[self.length - 1]  # del deletes a name(var reference) from current namespace
        self.length -= 1

        return last_item

    def delete_item(self, index):  # O(n)
        # ref item by index, shift items left from index to the end, remove last item, decrement length, return item
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        item = self.data[index]

        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]  # overrite items by 1 to left

        del self.data[self.length - 1]  # drop the last item
        self.length -= 1

        return item

    def insert_item(self, index, value):  # O(n)
        # extend list, increment length, shift items right from the end to index, insert new item
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        self.data[self.length] = None
        self.length += 1

        for i in range(self.length - 1, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value

    def __str__(self):
        return (
            f"{__class__.__name__}, length: {self.length}, "
            f"data: {[self.data[i] for i in range(self.length)]}"
        )


my_arr = MyArray()
my_arr.append_item("a")
my_arr.append_item("b")
my_arr.append_item("c")
my_arr.append_item("d")
print(my_arr)
my_arr.insert_item(3, "Yes")
print(my_arr)
print(my_arr.get_item(0))


class Test:
    def __init__(self):
        self.length = 0  # track the length
        self.data = {}

    def get_item(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        return self.data[index]

    def append_item(self, item):
        # append at the end, increment length
        # [1, 2, 3, 4]  -> 5 {0: 1, 1: 2, 2: 3, 3: 4, 4: 5}
        self.data[self.length] = item
        self.length += 1
        return self

    def pop_item(self):
        # cannot pop from the empty array
        if self.length == 0:
            raise IndexError("Pop from empty list")

        # ref last item, remove from data, decrement length, return last item
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item
    
    def delete_item(self, index):
        # ref del item, shift items left from index to the end, delete the last item
        # [1, 2, 3, 4]
        item = self.data[index]  # keep optionaly

        for i in range(index, self.length - 1):  # 1 -> 2
            self.data[i] = self.data[i + 1]
    
        del self.data[index]

        return item

    def insert_item(self, index, item):
        # extend list with None, increment length, shift items right from the end to index, insert new item
        # [1, 2, 5, 3, 4] -> (index=2, item=5)
        self.data[self.length] = None
        self.length += 1

        for i in range(self.length - 1, index, -1): # 4 -> 3
            self.data[i] = self.data[i - 1]
    
        self.data[index] = item