# https://leetcode.com/problems/maximum-frequency-stack/
# Maximum Frequency Stack--Hard

# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]


class FreqStack:

    def __init__(self):
        self.map = {}
        self.stack = []

    def push(self, val: int) -> None:
        if(val in self.map):
            self.map[val] += 1
        else:
            self.map[val] = 1

        temp = []
        while(self.stack and self.map[val] < self.stack[-1][1]):
            temp.append(self.stack.pop())

        self.stack.append((val, self.map[val]))

        while(temp):
            self.stack.append(temp.pop())

    def pop(self) -> int:
        x = self.stack.pop()[0]

        if(x in self.map):
            self.map[x] -= 1

        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
