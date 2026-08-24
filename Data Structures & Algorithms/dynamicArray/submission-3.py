class DynamicArray:
    
    def __init__(self, capacity: int):
        self.darr = [0] * capacity
        self.capacity = capacity
        self.size = 0


    def get(self, i: int) -> int:
        return self.darr[i]


    def set(self, i: int, n: int) -> None:
        self.darr[i] = n


    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        
        self.darr[self.size] = n
        self.size += 1


    def popback(self) -> int:
        self.size -= 1
        return self.darr[self.size]
 

    def resize(self) -> None:
        self.darr = self.darr + [0]*self.capacity
        self.capacity *= 2


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
