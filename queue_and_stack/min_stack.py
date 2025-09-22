from typing import Union 

class MinStack:

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.data) == 0 :
            self.min.append(val)
        elif self.min[-1] > val:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
            
        self.data.append(val)
        
    def pop(self) -> None:
        if self.data:
            self.data.pop(-1)
        if self.min:
            self.min.pop(-1)
        
    def top(self) -> Union[int, None]:
        if self.data:
            return self.data[-1]
        return None

    def getMin(self) -> Union[int, None]:
        if self.min:
            return self.min[-1]
        return None