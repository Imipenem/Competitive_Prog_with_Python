import collections
from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))  #timestamps are strictly increasing!!!

    def get(self, key: str, timestamp: int) -> str:
        A = self.time_map.get(key, None)
        if A is None: return ""
        i = bisect.bisect(A, (timestamp, chr(127)))
        return A[i - 1][1] if i else ""

if __name__ == "__main__":
    map = TimeMap()
    map.set("foo","bar",1)
    map.set("foo", "bar2", 7)
    map.set("foo", "bar4", 10)

    all_pairs = map.time_map.get("foo", None)
    idx = bisect.bisect(all_pairs, (2, chr(127)))

    #print(map.time_map["foo"][1][1])
    #print(bisect(map.time_map["foo"], (2, )))
    #print(bisect.bisect(all_pairs,(timestamp,chr(127))))

    print(map.get("foo",2))
