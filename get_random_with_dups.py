from collections import defaultdict
import bisect
import random

class RandomizedCollection:

    def __init__(self):
        self.store = defaultdict(int)
        self.mh = []

    def insert(self, val: int) -> bool:
        ret = val not in self.store
        bisect.insort_left(self.mh, val)

        self.store[val] += 1

        return ret

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False

        index = bisect.bisect_left(self.mh, val)
        self.mh.pop(index)
        self.store[val] -= 1
        if self.store[val] == 0:
            self.store.pop(val, None)
        return True

    def getRandom(self) -> int:
        return random.choice(self.mh)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
