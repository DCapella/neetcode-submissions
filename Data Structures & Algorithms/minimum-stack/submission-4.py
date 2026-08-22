class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.min) > 0 and val <= self.min[len(self.min)-1]:
            self.min.append(val)
        elif len(self.min) == 0:
            self.min.append(val)
        self.arr.append(val)

    def pop(self) -> None:
        if len(self.arr) >0:
            p = self.arr.pop()
            if self.min[len(self.min)-1] == p:
                self.min.pop()

    def top(self) -> int:
        return self.arr[len(self.arr)-1]

    def getMin(self) -> int:
        return self.min[len(self.min)-1]