class MinStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, val: int) -> None:
        self.q1.append(val)

        if not self.q2 or val <= self.q2[-1]:
            self.q2.append(val)

    def pop(self) -> None:
        removed = self.q1.pop()
        if removed == self.q2[-1]:
            self.q2.pop()

    def top(self) -> int:
        return self.q1[-1]

    def getMin(self) -> int:
        return self.q2[-1]
        
