class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.normal_stack = list()
        self.min_stack = list()
        

    def push(self, val: int) -> None:
        self.normal_stack.append(val)
        if len(self.min_stack)==0:
            self.min_stack.append(val)
        else:   
            min_ele = min(self.min_stack[-1],val)
            self.min_stack.append(min_ele)
        
        

    def pop(self) -> None:
        self.normal_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.normal_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]


