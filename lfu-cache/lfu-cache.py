class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.fq_list = deque()
        self.fq_dict = {}
        self.keys = {}
        self.idx_move = 0

    def get(self, key: int) -> int:
        if key in self.keys:
            fq = self.keys[key]
            idx = self.fq_dict[fq][0] + self.idx_move
            value = self.fq_dict[fq][1].pop(key)
            self.fq_dict[fq][0] -= 1
            fq += 1
            self.keys[key] = self.fq_list[idx] = fq
            if idx < len(self.fq_list)-1 and self.fq_list[idx+1] == fq:
                self.fq_dict[fq][1][key] = value
            else:
                self.fq_dict[fq] = [idx - self.idx_move, OrderedDict({key: value})]
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.c == 0:
            return
        if key in self.keys:
            fq = self.keys[key]
            idx = self.fq_dict[fq][0] + self.idx_move
            del self.fq_dict[fq][1][key]
            self.fq_dict[fq][0] -= 1
            fq += 1
            self.keys[key] = self.fq_list[idx] = fq
            if idx < len(self.fq_list)-1 and self.fq_list[idx+1] == fq:
                self.fq_dict[fq][1][key] = value
            else:
                self.fq_dict[fq] = [idx - self.idx_move, OrderedDict({key: value})]
        else:
            if len(self.fq_list) == self.c:
                LFq = self.fq_list.popleft()
                LFKey = next(iter(self.fq_dict[LFq][1]))
                del self.fq_dict[LFq][1][LFKey]
                del self.keys[LFKey]
                self.idx_move -= 1
            self.idx_move += 1
            self.keys[key] = 1
            if self.fq_list and self.fq_list[0] == 1:
                self.fq_dict[1][1][key] = value
            else:
                self.fq_dict[1] = [-self.idx_move, OrderedDict({key: value})]
            self.fq_list.appendleft(1)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value) 
