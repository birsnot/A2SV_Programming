class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.dic = {}

    def get(self, key: int) -> int:
        if key in self.dic:
            value = self.dic.pop(key)
            self.dic[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            del self.dic[key]
        elif len(self.dic) == self.c:
            LCU_key = next(iter(self.dic))
            del self.dic[LCU_key]
        self.dic[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
