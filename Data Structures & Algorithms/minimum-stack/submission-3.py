class MinStack:

    def __init__(self):
        self.stack = []
        self.previous = []
        self.min = None
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min is None:
            self.min = val
        elif val <= self.min:
            self.previous.append(self.min)
            self.min = val
        elif self.previous and val <= self.previous[-1]:
            self.previous.append(val)
        
        

    def pop(self) -> None:
        gone = self.stack.pop()
        if self.min == gone:
            if self.previous:
                self.min = self.previous.pop()
            else:
                self.min = None
        elif self.previous and self.previous[-1] == gone:
            self.previous.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
