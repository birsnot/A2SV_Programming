class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0]*k
        self.st = 0
        self.len_ = 0
        self.K = k

    def enQueue(self, value: int) -> bool:
        if self.len_ < self.K:
            self.q[(self.len_ + self.st)%self.K] = value
            self.len_ += 1
            return True

    def deQueue(self) -> bool:
        if self.len_:
            self.st += 1
            self.st %= self.K
            self.len_ -= 1
            print(self.st, self.len_)
            return True

    def Front(self) -> int:
        if self.len_:
            return self.q[self.st]
        return -1

    def Rear(self) -> int:
        if self.len_:
            return self.q[(self.st + self.len_ - 1)%self.K]
        return -1        

    def isEmpty(self) -> bool:
        return self.len_ == 0

    def isFull(self) -> bool:
        return self.len_ == self.K


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()