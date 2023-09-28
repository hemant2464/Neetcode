import bisect
class Item:
    def __init__(self):
        self.time = []
        self.contents = {}

class TimeMap:

    def __init__(self):
        self._dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        content = self._dict.get(key, None)
        if not content:
            new_item = Item()
            new_item.time.append(timestamp)
            new_item.contents[timestamp] = value
            self._dict[key] = new_item
        else:
            content.time.append(timestamp)
            content.contents[timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._dict:
            return ""
        candidates = self._dict[key]
        last_times = candidates.time[-1]
        if last_times <= timestamp:
            get_time = last_times
        elif timestamp >= candidates.time[0]:
            idx = bisect.bisect_right(candidates.time, timestamp)
            get_time = candidates.time[idx-1]
        else:
            return ""
        return candidates.contents[get_time]