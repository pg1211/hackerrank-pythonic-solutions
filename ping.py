import bisect

# in this problem: return number of pings that have occurred in the last 3000 ms from the time of insertion.
# include the ping being appended.

class RecentCounter:

    def __init__(self):
        self.times = []  # timestamps entered

    def ping(self, t: int) -> int:
        self.times.append(t)

        index = bisect.bisect_left(self.times, t - 3000)

        n = len(self.times) - index
        self.times = self.times[index:]

        return n


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
