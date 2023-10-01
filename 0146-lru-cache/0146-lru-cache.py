from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move the accessed key to the end to indicate it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update the value and move the key to the end
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                # Remove the first item (least recently used)
                self.cache.popitem(last=False)
            # Add the new key-value pair to the cache
            self.cache[key] = value