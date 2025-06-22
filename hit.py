import bisect

# in this problem: return hits from the last 300 seconds from timestamp passed in.
# all calls will be made with increasing timestamps.

class HitCounter:

    def __init__(self):
        self.hits = []  # list of timestamps

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    # return number of hits from last 300 seconds from timestamp
    # get hits in range [ts - 300, ts] inclusive
    def getHits(self, timestamp: int) -> int:
        left = bisect.bisect_left(self.hits, timestamp - 300 + 1)

        return len(self.hits) - left
