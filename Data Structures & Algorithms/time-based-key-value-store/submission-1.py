from bisect import *
class TimeMap:
    

    def __init__(self):
        self.values = defaultdict(list)

        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        pos = bisect_right(self.values[key], timestamp, key=lambda x: x[0]) - 1

        if pos == -1:
            return ""

        return self.values[key][pos][1]

