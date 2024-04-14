'''stack by deque'''

from collections import deque

class FreqStack:
    '''class for stack'''
    def __init__(self):
        '''init'''
        self.stack = deque()
        self.frequency = deque()

    def push(self, val: int) -> None:
        '''push element to stack'''
        self.stack.append(val)
        self.frequency.append(self.stack.count(val)+1)

    def pop(self):
        '''pop most frequent element from stack'''
        self.stack.reverse()
        self.frequency.reverse()
        max_value = max(self.frequency)
        idx = self.frequency.index(max_value)
        counter=0

        for el in self.stack:
            if counter == idx:
                val = el
                self.stack.remove(el)
                self.frequency.remove(max_value)
                break
            counter+=1

        self.stack.reverse()
        self.frequency.reverse()

        return val
