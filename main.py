# Змініть стек із першого завдання таким чином, щоб його
# розмір був нефіксованим.


class Stack:
    def __init__(self, ):
        self.stack = []


    def push(self, item):
        self.stack.append(item)
        return self.stack


    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def last_elem(self):
        return self.stack[-1]


stack = Stack()
stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")
stack.push("5")
print(f"Last element of stack: {stack.last_elem()}")
print(f"Deleted element is: {stack.pop()}")
print(f"Stack size is: {stack.size()}")
stack.push("1")
stack.push("2")
stack.clear()
