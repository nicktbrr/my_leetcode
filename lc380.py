class RandomizedSet:

    def __init__(self):
        self.my_set = {}

    def insert(self, val: int) -> bool:
        if val not in self.my_set:
            self.my_set[val] = 1
            return True
        else:
            False

    def remove(self, val: int) -> bool:
        if val not in self.my_set:
            return False
        else:
            self.my_set.pop(val)
            return True

    def getRandom(self) -> int:
        rand = random.randint(0, len(self.my_set) - 1)
        return list(self.my_set.keys())[rand]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()