class MyCircularQueue:

    def __init__(self, k: int):
        self.maxLen = k
        self.queue = [-1]*k
        self.front=0
        self.rear=-1
        self.available = k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.maxLen
        self.available -= 1
        self.queue[self.rear] = value
        print(self.queue)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        position = self.front 
        self.front = (self.front +1) % self.maxLen
        self.available += 1
        self.queue[position] = -1
        
        return True
        

    def Front(self) -> int:
        return self.queue[self.front]
        

    def Rear(self) -> int:
        return self.queue[self.rear]
        

    def isEmpty(self) -> bool:
        return self.available == self.maxLen        
        
        

    def isFull(self) -> bool:
        return self.available == 0
        
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()