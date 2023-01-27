class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.len = 0
        self.dummy = Node()
        self.tail = None

    def get(self, index: int) -> int:
        if 0 <= index < self.len:
            cur = self.dummy.next
            for _ in range(index):
                cur = cur.next
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        if self.len == 1:
            self.tail = self.dummy.next

    def addAtTail(self, val: int) -> None:
        if self.len == 0:
            self.addAtHead(val)
        else:
            new_tail = Node(val)
            self.tail.next = new_tail
            self.tail = new_tail
            self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.len and index == self.len:
            self.addAtTail(val)
        elif 0 <= index <= self.len:
            cur = self.dummy
            for _ in range(index):
                cur = cur.next
            new_node = Node(val, cur.next)
            cur.next = new_node
            self.len += 1
    
    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index and index < self.len:
            cur = self.dummy
            for _ in range(index):
                cur = cur.next
            if index == self.len - 1:
                self.tail = cur
            temp = cur.next
            cur.next = cur.next.next
            del temp
            self.len -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)