class StockSpanner:

    def __init__(self):
        self.prices = []
        self.mono_stk = []
        self.len_ = 0

    def next(self, price: int) -> int:
        while self.mono_stk and self.prices[self.mono_stk[-1]] <= price:
            self.mono_stk.pop()
        if self.mono_stk:
            ret = self.len_ - self.mono_stk[-1]
        else:
            ret = self.len_ + 1
        self.mono_stk.append(self.len_)
        self.prices.append(price)
        self.len_ += 1
        return ret


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)