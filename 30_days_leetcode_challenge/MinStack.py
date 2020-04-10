class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        if not self.min or x <= self.min[-1]:  # only those <= to actual min must be taken into account, other will be popped before
            # and wont ever be the minimum
            self.min.append(x)

    def pop(self) -> None:
        if self.min[-1] == self.top():
            self.min.pop(-1)
        self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def getMin(self) -> int:
        return self.min[-1]

if __name__ == '__main__':


    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())  # --> Returns -3.
    minStack.pop()
    print(minStack.top())  #    --> Returns 0.
    print(minStack.getMin()) #   --> Returns -2.
