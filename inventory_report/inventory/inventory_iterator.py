from collections.abc import Iterator


class InventoryIterator(Iterator):
    @classmethod
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):

        if self.index > len(self.data):
            raise StopIteration()

        current = self.data[self.index]
        self.index += 1
        return current

