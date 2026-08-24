class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def push(self, x: int) -> None:
        node = Node(x)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = node.next

    def pop(self) -> int:
        cur = self.head
        self.head = self.head.next
        return cur.val

    def top(self) -> int:
        return self.head.val
        

    def empty(self) -> bool:
        return self.head is None
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()