class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = [0]*5001
        self.st = 2000
        self.k = k
        self.len_ = 0

    def insertFront(self, value: int) -> bool:
        if self.len_ == self.k:
            return False
        self.st -= 1
        self.dq[self.st] = value
        self.len_ += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len_ == self.k:
            return False
        self.dq[self.st + self.len_] = value
        self.len_ += 1
        return True

    def deleteFront(self) -> bool:
        if self.len_:
            self.st += 1
            self.len_ -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.len_:
            self.len_ -= 1
            return True
        return False

    def getFront(self) -> int:
        if self.len_:
            return self.dq[self.st]
        return -1

    def getRear(self) -> int:
        if self.len_:
            return self.dq[self.st + self.len_ - 1]
        return -1

    def isEmpty(self) -> bool:
        return self.len_ == 0

    def isFull(self) -> bool:
        return self.len_ == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()