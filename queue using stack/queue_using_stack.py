class Node:
    '''class node'''
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    '''stack'''
    def __init__(self):
        '''init stack'''
        self.top = None

    def push(self, value):
        '''push node to stack'''
        node = Node(value)
        if not self.top:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pull(self):
        '''pull node'''
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None

class MyQueue:
    '''class queue by stack'''
    def __init__(self):
        '''init'''
        self.main = Stack()
        self.copy = Stack()        

    def push(self, x: int) -> None:
        '''push node to queue'''
        self.main.push(x)

    def pop(self) -> int:
        value = None
        while self.main.top:
            if not self.main.top.next:
                value = self.main.top.value
            else:
                self.copy.push(self.main.top.value)
            self.main.pull()

        while self.copy.top:
            self.main.push(self.copy.top.value)
            self.copy.pull()

        return value

    def peek(self) -> int:
        value = None
        while self.main.top:
            if not self.main.top.next:
                value = self.main.top.value
            self.copy.push(self.main.top.value)
            self.main.pull()

        while self.copy.top:
            self.main.push(self.copy.top.value)
            self.copy.pull()

        return value

    def empty(self) -> bool:
        return self.main.top is None

# Your MyQueue object will be instantiated and called as such:
# MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
# [[],[1],[2],[3],[4],[],[5],[],[],[],[]]
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.pop())
obj.push(5)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
