class MyStack:

    def __init__(self):
        self.q = []
        

    def push(self, x: int) -> None:
        self.q = [x] + self.q
        

    def pop(self) -> int:
        t = self.q[0]
        self.q = self.q[1:]
        return t
        

    def top(self) -> int:
        return self.q[0]
        

    def empty(self) -> bool:
        return self.q == []
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()