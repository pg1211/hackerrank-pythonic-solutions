from collections import defaultdict
import bisect

# Design a time-based key-value data structure that can store multiple values for 
# the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
# If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)  # {key: [(timestamp, value)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]

        if not lst or timestamp < lst[0][0]:
            return ""

        if timestamp > lst[len(lst) - 1][0]:
            return lst[len(lst) - 1][1]

        index = bisect.bisect_left([ts for ts, _ in lst], timestamp)

        if lst[index - 1][0] < timestamp < lst[index][0]:
            return lst[index - 1][1]

        return lst[index][1] if index < len(lst) else lst[index - 1][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# tm = TimeMap()
# tm.set("foo", "bar", 1)
# tm.set("foo", "baz", 2)
# tm.set("foo", "bay", 3)
# tm.get("foo", 1)
# tm.get("foo", 2)
# tm.get("foo", 6)
