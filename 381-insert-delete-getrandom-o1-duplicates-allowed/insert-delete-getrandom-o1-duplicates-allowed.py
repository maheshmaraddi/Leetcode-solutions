import random

class RandomizedCollection:

    def __init__(self):
        self.l = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            self.l.append(val)
            self.d[val] += 1
            return False
        else:
            self.l.append(val)
            self.d[val] = 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            self.l.remove(val)
            self.d[val] -= 1
            if self.d[val] == 0:
                del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        return self.l[random.randint(0, len(self.l) - 1)]



# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()